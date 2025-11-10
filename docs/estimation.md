# Raw Estimation and ETA

## **Phase 1: Setup and Environment Configuration**
- **Tasks**:
  - Set up the development environment (Python, libraries, and tools).
  - Install required libraries (e.g., `requests`, `BeautifulSoup`, `openai`, `langchain`, `chromadb`, etc.).
  - Set up API access for the chosen GenAI platform OpenAI.
  - Configure a vector database ChromaDB.
- **Estimated Time**: 1 day

| Event | Date/Time         |
|-------|-------------------|
| Start | 11/10/2025 9:00   |
| End   |                   |

## **Phase 2: News Scraping**
- **Tasks**:
  - Implement a script to scrape news articles from the given URLs.
  - Extract headlines and full text from the articles.
  - Handle edge cases (e.g., missing content, dynamic content loading).
  - Test scraping on multiple URLs to ensure robustness.
- **Estimated Time**: 2 days

## **Phase 3: GenAI-driven Summarization and Topic Identification**
- **Tasks**:
  - Use a GenAI platform (e.g., OpenAI GPT) to generate summaries of the articles.
  - Use the same or additional GenAI tools to identify the main topics of the articles.
  - Integrate the summarization and topic identification processes into the pipeline.
  - Test and validate the quality of the generated summaries and identified topics.
- **Estimated Time**: 2 days

## **Phase 4: Storing Data in a Vector Database**
- **Tasks**:
  - Store the extracted articles, summaries, and topics in a vector database.
  - Use embeddings (e.g., OpenAI embeddings or Sentence Transformers) to represent the data in vector form.
  - Ensure the database is properly indexed for efficient semantic search.
- **Estimated Time**: 1 day

## **Phase 5: Semantic Search Implementation**
- **Tasks**:
  - Implement a semantic search feature using the vector database and embeddings.
  - Integrate GenAI tools to interpret user queries and match them with relevant articles based on summaries and topics.
  - Handle semantically close terms (e.g., synonyms) in the search process.
  - Test the search functionality with various queries to ensure accuracy and relevance.
- **Estimated Time**: 2 days

## **Phase 6: Final Testing and Documentation**
- **Tasks**:
  - Perform end-to-end testing of the entire pipeline.
  - Fix any bugs or edge cases discovered during testing.
  - Write a comprehensive `README.md` file with setup instructions, usage details, and examples.
  - Upload the code to a GitHub repository.
- **Estimated Time**: 1 day

## **Total Estimated Time**: **9 days**

## **Deliverables**
1. **GitHub Repository**:
   - Python scripts for all components (scraping, summarization, topic identification, semantic search).
   - `README.md` file with:
     - Setup instructions.
     - Usage guide.
     - Examples of input URLs and corresponding output (summaries, topics, and search results).

2. **Fully Functional Prototype**:
   - End-to-end working solution that scrapes news articles, generates summaries and topics, stores them in a vector database, and provides semantic search functionality.

## **Assumptions**
1. URLs provided will be valid and accessible.
2. OpenAI GPT or equivalent GenAI platform will be used for summarization and topic identification.
3. A free-tier or trial version of a vector database like Pinecone or ChromaDB can be used for this task.
4. No additional UI/UX or deployment is required (e.g., no web app or API unless explicitly stated).
