# **News Scraping, Summarization, and Semantic Search**

This project is designed to extract news articles from provided URLs, summarize them, identify main topics using Generative AI (GenAI), and enable semantic search over the processed articles. The goal is to demonstrate the use of GenAI tools, vector databases, and semantic search techniques in a practical application.

## **Features**
1. **News Scraping**: 
   - Extract full-text articles and headlines from the provided URLs.
2. **GenAI-Powered Summarization and Topic Identification**:
   - Generate concise summaries of the articles.
   - Identify main topics using Generative AI tools (e.g., OpenAI GPT models).
3. **Semantic Search**:
   - Store articles, summaries, and topics in a vector database.
   - Implement a semantic search feature that understands user queries and retrieves relevant articles based on context.

## **Tech Stack**
- **Programming Language**: Python
- **Libraries**:
  - Web scraping: `requests`, `beautifulsoup4`
  - GenAI integration: `openai`, `langchain`
  - Vector database: `pinecone-client`, `chromadb`, `faiss-cpu`
  - Embedding generation: `sentence-transformers`
  - Environment variable management: `python-dotenv`
  - Testing: `pytest`
  - Utilities: `numpy`, `pandas`, `tqdm`

## **Installation**

### **Prerequisites**
- Python 3.8 or higher
- Pip (Python package manager)
- API keys for:
  - [OpenAI](https://platform.openai.com/signup/) (for GPT models and embeddings)
  - [Pinecone](https://www.pinecone.io/) (if using Pinecone for vector database)

### **Steps**

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/news-scraping-genai-project.git
   cd news-scraping-genai-project
   ```

2. **Set Up a Virtual Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   Install all required libraries from `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**
   Create a `.env` file in the root directory and add your API keys and database credentials:
   ```plaintext
   OPENAI_API_KEY=your_openai_api_key
   PINECONE_API_KEY=your_pinecone_api_key
   PINECONE_ENVIRONMENT=your_pinecone_environment
   ```

5. **Run the Project**
   Execute the pipeline from the command line:
   ```bash
   python src/main.py
   ```

## **Usage**

### **Input**
- A list of URLs pointing to news articles.

### **Output**
- **Summaries**: Concise summaries of the articles.
- **Topics**: Main topics identified for each article.
- **Semantic Search**: Ability to query articles using natural language and retrieve relevant results.

### **Example**
1. **Input**:
   ```plaintext
   https://example-news-site.com/article1
   https://example-news-site.com/article2
   ```
2. **Output**:
   - **Summaries**:
     - *Article 1*: "This article discusses the impact of climate change on global agriculture..."
     - *Article 2*: "The latest advancements in AI technology are transforming industries..."
   - **Topics**:
     - *Article 1*: ["Climate Change", "Agriculture", "Global Warming"]
     - *Article 2*: ["AI", "Technology", "Innovation"]

3. **Semantic Search**:
   - **Query**: "How is AI changing industries?"
   - **Result**: Returns *Article 2* as the most relevant result.

## **Project Structure**

```plaintext
news-scraping-genai-project/
│
├── data/                             # Directory for storing raw and processed data
│   ├── raw_articles/                 # Raw scraped articles (optional, for debugging)
│   ├── processed_articles/           # Processed articles with summaries and topics
│   └── embeddings/                   # Embedding files (optional, for debugging)
│
├── src/                              # Source code directory
│   ├── scraping/                     # Scripts for news scraping
│   │   ├── scraper.py                # Main scraping logic
│   │   ├── parser.py                 # Helper functions for parsing HTML
│   │   └── __init__.py               # Init file for scraping module
│   │
│   ├── genai/                        # Scripts for GenAI integration
│   │   ├── summarizer.py             # Summarization logic using GenAI
│   │   ├── topic_identifier.py       # Topic extraction logic using GenAI
│   │   └── __init__.py               # Init file for GenAI module
│   │
│   ├── db/                           # Scripts for vector database integration
│   │   ├── vector_store.py           # Logic to interact with vector database
│   │   ├── embeddings.py             # Script to generate embeddings
│   │   └── __init__.py               # Init file for database module
│   │
│   ├── search/                       # Scripts for semantic search
│   │   ├── semantic_search.py        # Semantic search logic
│   │   └── __init__.py               # Init file for search module
│   │
│   ├── config.py                     # Configuration variables (API keys, database URLs, etc.)
│   ├── main.py                       # Main script to run the entire pipeline
│   └── utils.py                      # Utility functions (e.g., logging, error handling)
│
├── requirements.txt                  # List of Python dependencies
├── README.md                         # Project documentation
├── .env                              # Environment variables (e.g., API keys, database credentials)
├── .gitignore                        # Files and folders to ignore in Git
└── tests/                            # Test cases
    ├── test_scraper.py               # Unit tests for scraping module
    ├── test_genai.py                 # Unit tests for GenAI module
    ├── test_db.py                    # Unit tests for database module
    ├── test_search.py                # Unit tests for search module
    └── __init__.py                   # Init file for tests module
```

## **How It Works**

1. **Scraping**:
   - The `scraper.py` script extracts the full text and headline from the provided article URLs.
   - The parsed content is cleaned and stored in the `data/raw_articles/` directory for debugging purposes.

2. **Summarization and Topic Identification**:
   - The `summarizer.py` script uses OpenAI GPT (or another GenAI tool) to generate concise summaries of the articles.
   - The `topic_identifier.py` script extracts the main topics of each article using GenAI tools.

3. **Vector Database**:
   - The `vector_store.py` script stores the articles, summaries, and topics as embeddings in a vector database (e.g., Pinecone, ChromaDB, or FAISS).
   - The `embeddings.py` script generates embeddings using OpenAI embeddings or Sentence Transformers.

4. **Semantic Search**:
   - The `semantic_search.py` script allows users to input natural language queries.
   - The vector database is queried using embeddings generated from the input query, returning the most relevant articles.

## **Testing**

Run the unit tests using `pytest`:

```bash
pytest tests/
```

## **Future Enhancements**
- Add support for more GenAI platforms (e.g., Hugging Face models).
- Add a web-based user interface for easier interaction.
- Implement support for additional vector databases (e.g., Weaviate, Milvus).
- Add support for real-time news scraping from RSS feeds or APIs.

## **Contributing**
Feel free to contribute to this project by submitting issues or pull requests. For major changes, please open an issue first to discuss what you would like to change.

## **License**
This project is licensed under the MIT License.

## **Contact**
For any questions or suggestions, feel free to reach out:

- **Name**: Viktor Tovstyi
- **Email**: Viktor_Tovstyi@epam.com
- **GitHub**: 
