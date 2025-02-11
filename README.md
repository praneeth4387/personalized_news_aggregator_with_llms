# **Personalized News Aggregator**  

## **Introduction**  
The **Personalized News Aggregator** is a Python-based application that **collects, processes, categorizes, and serves news articles** from sources like **BBC and CNN**. Users can **retrieve articles based on filters** and access them through a **FastAPI-powered web interface**.  

---

## **Project Overview**  
This project **automates web scraping**, processes news data, and provides a **user-friendly API** for retrieving and searching news articles. It combines **web scraping, NLP-based preprocessing, and API development** to deliver a structured news experience.  

---

## **Key Features**  
- **Web Scraping** – Dynamically collects news articles from BBC & CNN.  
- **Data Preprocessing** – Summarizes and cleans articles using NLP techniques.  
- **AI-Powered Categorization** – Uses **Gemini LLM** for topic classification.  
- **FastAPI Endpoints** – Provides structured access to news data.  
- **Web Interface** – Allows **users to search & interact** with news content.  

---

## **Technology Stack**  
- **Python 3.12.6**  
- **FastAPI** – Web API framework  
- **Pandas** – Data processing & storage  
- **Selenium & BeautifulSoup** – Web scraping  
- **Gemini LLM** – AI-based article categorization  
- **Uvicorn** – ASGI server for FastAPI  

---

## **Overview of Code Files**  
- **`news_aggregator.py`** – Implements **FastAPI endpoints** for serving news.  
- **`news_extractor.py`** – Scrapes news from **BBC & CNN** dynamically.  
- **`news_categorization.py`** – Categorizes articles using **AI-based NLP techniques**.  
- **`news_articles.csv`** – Stores extracted & categorized articles.  
- **`requirements.txt`** – Lists dependencies for easy installation.  

---

## **API Endpoints**  

### **Root (`/`)**  
- **Description:** Serves the homepage with navigation links.  
- **Method:** `GET`  
- **Response:** HTML page with links to key API routes.  

### **Articles (`/articles`)**  
- **Description:** Fetches & displays all stored news articles.  
- **Method:** `GET`  
- **Response:** JSON content of all articles.  

### **Article by ID (`/article-id/{id}`)**  
- **Description:** Fetches a specific article using its **unique ID**.  
- **Method:** `GET`  
- **Parameters:**  
  - `id` (int) → Article ID  
- **Response:** JSON content of the requested article.  

### **Search Articles (`/search/{key}/{value}`)**  
- **Description:** Filters articles based on **title, summary, date, source, or category**.  
- **Method:** `GET`  
- **Parameters:**  
  - `key` (str) → Field to search (e.g., **title, summary, category**)  
  - `value` (str) → Search term  
- **Response:** JSON content of **matching articles**.  

---

## **Installation & Execution**  

### **Prerequisites**  
Ensure you have **Python 3.12.6** installed.  

### **Install Dependencies**  
```bash
pip install -r requirements.txt
```

### **Running the Application**  
```bash
uvicorn news_aggregator:app --reload
```
- **FastAPI server starts on:** [`http://127.0.0.1:8000/`](http://127.0.0.1:8000/)  
- **API Documentation:** [`http://127.0.0.1:8000/docs`](http://127.0.0.1:8000/docs)  

---

## **Deployment**  
This project is **open-source and hosted on GitHub** for further improvements. 

---

## **Best Practices**  

### **API Design Guidelines**  
- Keep endpoints intuitive and consistent (e.g., `/articles`, `/article-id/{id}`, `/search/{key}/{value}`).  
- Follow RESTful standards for better usability.  

### **Efficient Data Handling**  
- Store articles in a **CSV file** for lightweight storage and scalability.  
- Preprocess summaries before storing to avoid excessive computations.  

### **Error Handling**  
- Return **meaningful error messages** when an article is not found.  
- Example: `{ "error": "Article not found" }`  
- Handle **web scraping failures gracefully** by skipping faulty articles.  

---

## **Future Enhancements**  

### **Adding More News Sources**  
- Expand to sources like **Reuters, Al Jazeera, and other global outlets**.  

### **Improving Search Functionality**  
- Implement **fuzzy search** (typo tolerance).  
- Add **date range filters** and **multi-category searches**.  

### **Expanding to Other Data Formats**  
- Support **JSON/XML storage** for structured data retrieval.  
- Integrate **SQL databases** for better scalability.  

---

## **Conclusion**  

The **Personalized News Aggregator** successfully:  
✅ **Scrapes & processes news articles** from multiple sources.  
✅ **Uses AI-powered categorization** for better content organization.  
✅ **Provides a user-friendly FastAPI service** for seamless access.  

### **🚀 Future improvements will focus on:**  
✔ Expanding to **more news sources**.  
✔ Enhancing **search & filtering options**.  
✔ Supporting **new data storage formats** for scalability.  

---

## **Final Enhancements in This Version**  
✔ **Execution video removed** (as execution has changed).  
✔ **Improved clarity & structure** – More concise and professional.  
✔ **Future-ready** – Supports **scalability, additional sources, and AI enhancements**.  

---

