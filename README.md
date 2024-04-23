Abstract 

This project aimed to create a focused web crawler for information retrieval. 
The crawler targets Wikipedia articles and creates a basic document index to 
help with information retrieval.  
Development Summary: The crawler uses the Scrapy framework to navigate 
and download Wikipedia articles. The downloaded pages are parsed with 
BeautifulSoup to extract text content. The extracted text goes through cleaning 
steps to remove irrelevant information and prepare it for further processing. 
Finally, a TF-IDF vectorizer and cosine similarity are used to generate a 
document index that records the relationships between crawled articles.  
Objectives:The primary goal was to design and implement a web crawler 
capable of navigating Wikipedia and creating a basic document index. This 
index helps users find relevant articles based on content similarity.  
Next steps: Future improvements could include extending the crawling scope 
beyond Wikipedia.  
Implementing user queries and retrieval of relevant documents.  
Improving the text cleaning process for better information extraction.  
Investigate advanced indexing techniques such as Latent Semantic Indexing 
(LSI).  

Overview 

This project creates a framework for a focused crawler that uses Wikipedia for 
information retrieval tasks.  
Solution Outline: The solution makes use of Scrapy's web scraping capabilities. 
BeautifulSoup helps you parse the downloaded HTML content and extract 
relevant text. Text cleaning techniques get the extracted text ready for further 
processing. Finally, TF-IDF and cosine similarity generate a document index 
that captures the semantic relationships between articles.  
Relevant Literature: The project is based on concepts from web scraping using 
frameworks such as Scrapy [reference Scrapy documentation]. It also uses 
Natural Language Processing (NLP) techniques such as text cleaning and TF
IDF, which are commonly used in information retrieval tasks.  
The proposed system is a specialized web crawler designed specifically for 
Wikipedia. It retrieves and indexes documents, which allows users to find 
articles. 

Design 

The design focuses on crawling, text extraction, and document indexing.  
System Capabilities:  
Crawling Wikipedia articles to a specific depth limit.  
Extracting text from downloaded HTML pages.  
Cleaning the extracted text to remove any unnecessary information.  
Creating a document index with TF-IDF and cosine similarity for document 
retrieval.  
Interactions: The system uses Wikipedia to download articles. It also interacts 
with the user via an interface (to be developed in subsequent steps) that accepts 
queries and returns retrieved documents.  
Scrapy for web scraping, BeautifulSoup for HTML parsing, re libraries for text 
cleaning, and scikit-learn for TF-IDF and cosine similarity calculations are all 
integrated into the system.  

Architecture 

The architecture is made up of multiple software components that work together 
to achieve desired functionality.  
Components: Scrapy Spider: Manages crawling logic, links, and webpage 
downloads.  
Parser uses BeautifulSoup to extract text content from downloaded HTML.  
Text Cleaner uses regular expressions to remove HTML tags, escape characters, 
and irrelevant symbols.  
Indexer: Uses scikit-learn's TF-IDF vectorizer to generate a document-term 
matrix and compute cosine similarities between documents.  
Interfaces: The current system communicates with Wikipedia as its data source. 
Future development will include designing a user interface to accept queries and 
display retrieved documents.  
The code makes use of Python libraries such as Scrapy, BeautifulSoup, re, and 
scikit-learn. The extracted data is saved in a pickled file for later use.  

Operation 

Install Python and Install Linux in windows 
wsl –install 
Install required libraries 
Pip install scrapy 
Pip install sckit-learn 
pip install beautifulsoup4 
pip install flask 
pip install requests 

Installation: 

Scrapy Crawl: 
Navigate to the spiders folder in the terminal. 
Run the command: Scrapy crawl IRPROJECT
This step calculates TF-IDF scores and cosine similarity for the HTML 
documents, storing the results in an index.pkl file. 
Access the Index: 
Go to the access pickle folder in the terminal. 
Run the Python file to display the content of the index.pkl file. 
Start Flask Server: 
Navigate to the Flask folder in the terminal. 
Run the Python file to initiate the Flask server. 
Make a Query Request: 
Open a new terminal. 
Send a request to the Flask server with a query in the following format: 
curl -X POST http://localhost:5000/query -H "Content-Type: 
application/json" -d '{"query": "python introduction"}' 
The server will respond with a JSON format containing cosine similarity and 
document names of the top-k results 

Conclusion

Success: 

The crawler successfully crawls Wikipedia articles within the specified depth 
limit and builds a document index file (index.pkl) containing information about 
each crawled article, including its TF-IDF vector and cosine similarities with 
other articles. 

Failure: 

The script might encounter errors if: 
Required libraries are not installed. 
Wikipedia or the starting URL becomes inaccessible. 
There are issues with parsing specific HTML structures. 
Outputs: 
Upon successful completion, a pickled file (index.pkl) is created, storing the 
built document index. 

Caveats/Cautions: 

The current crawling depth is limited . Adjust it cautiously to avoid 
overwhelming Wikipedia's servers. 
The script focuses on text content and doesn't consider other elements like 
infoboxes or images, which might be relevant for information retrieval. 

Data Sources 

Scrapy - https://docs.scrapy.org/en/latest/ 

Beautiful Soup - https://beautiful-soup-4.readthedocs.io/en/latest/ 

Scikit-learn -  scikit-learn: machine learning in Python — scikit-learn 1.4.2 

documentation 

Flask - https://flask.palletsprojects.com/en/3.0.x/ 

Source Code 

Spider file - react_beauty_spider.py 

Scrapped pages - react-{id} 

Processor logic - processor.py 

Query logic - query.py 

Pickle file - tf-idf.pkl 

Programmatic API - manual-request.py 

Scikit API - scikit-request.py

Test Cases: 

![image](https://github.com/SSP24SCM80B/PROJECTIR/assets/163352430/16296301-6990-4e2e-8e44-7fa7fac746bd)
![image](https://github.com/SSP24SCM80B/PROJECTIR/assets/163352430/7e4ee9fd-5c51-44e6-a90b-79e60c53ff10)

![image](https://github.com/SSP24SCM80B/PROJECTIR/assets/163352430/aaf79629-5b6d-4690-b783-dfcc2c147ae7)
![image](https://github.com/SSP24SCM80B/PROJECTIR/assets/163352430/3ebc02ae-e2af-485e-a23a-1d88621804f6)



 
Bibliography 

https://requests.readthedocs.io/en/latest/ 

https://flask.palletsprojects.com/en/3.0.x/ 

https://scikit-learn.org/stable/ 

https://scrapy.org
