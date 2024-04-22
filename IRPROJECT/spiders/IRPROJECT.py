import scrapy
from pathlib import Path
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import re
class WikipediaCrawlerSpider(scrapy.Spider):
    name = 'IRPROJECT'
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/Python_(programming_language)']

    custom_settings = {
        'DEPTH_LIMIT': 2, 
        'CLOSESPIDER_PAGECOUNT': 10,  # Set maximum page count
    }
    page_count = 0
    documents = []
    document_names = []

    def parse(self, response):
        self.page_count += 1
        filename = self.get_valid_filename(response.url.split("/")[-1]) + '.html'
        self.document_names.append(filename)  # Store document name
        if self.page_count > self.settings.get('CLOSESPIDER_PAGECOUNT'):
            return
        if response.meta['depth'] > self.settings.get('DEPTH_LIMIT'):
            return
        with open(filename, "wb") as file:
            file.write(response.body)
        self.log(f"Saved file {filename}")

        with open(filename, "rb") as file:
            # Decode bytes to string using utf-8 encoding
            html_content = file.read().decode('utf-8')
            soup = BeautifulSoup(html_content, 'html.parser')
            text = soup.get_text()
            # Clean the text
            clean_text = self.clean_text(text)
            self.documents.append(clean_text)

        for next_page in response.css('a::attr(href)').getall():
            yield response.follow(next_page, callback=self.parse)

    def closed(self, reason):
        self.build_index()

    def build_index(self):
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform(self.documents)
        cosine_sim_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)

        index = {}
        for idx, (doc_name, doc) in enumerate(zip(self.document_names, self.documents)):
            index[idx] = {
                'document_name': doc_name,
                'document': doc,
                'tfidf_vector': tfidf_matrix[idx],
                'cosine_similarities': cosine_sim_matrix[idx]
            }

        with open('index.pkl', 'wb') as file:
            pickle.dump(index, file)

    def get_valid_filename(self, filename):
        # Remove invalid characters from filename
        return re.sub(r'[<>:"/\\|?*]', '_', filename)

    def clean_text(self, text):
        # Remove HTML tags
        clean_text = re.sub(r'<.*?>', '', text)
        # Remove escape characters
        clean_text = re.sub(r'\\[ntr]', '', clean_text)
        # Remove other special symbols
        clean_text = re.sub(r'[^a-zA-Z0-9\s]', '', clean_text)
        # Remove extra whitespaces
        clean_text = re.sub(r'\s+', ' ', clean_text)
        # Convert to lowercase
        clean_text = clean_text.lower()
        return clean_text
