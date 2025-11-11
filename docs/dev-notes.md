## Developer Notes

### Setup & Dependencies

- Create and activate your Python virtual environment:
  ```sh
  python -m venv .venv
  source .venv/bin/activate        # On Windows: .venv\Scripts\activate
  ```
- Install required packages:
  ```sh
  pip install -r requirements.txt
  ```
- ChromaDB: Ensure `sentence-transformers` and compatible `huggingface_hub` are installed for local vector search functionality.
- OpenAI: Set your API key as an environment variable (`OPENAI_API_KEY`) for embedding and summarization.

### Project Structure

See `docs/project-structure.md` for up-to-date folder and module map.

### Typical Workflow

1. **Load Articles:**
   - Use the CLI:  
     ```sh
     python src/main.py load "URL1" "URL2" ...
     ```
   - Each article receives a unique ID (uuid) and is optionally summarized.

2. **Find Articles (Semantic Search):**
   - Use the CLI:  
     ```sh
     python src/main.py find "search query" --top_k 3
     ```
   - Results include ID, title, text preview, similarity score.

### Extending the Pipeline

- **Adding New Models/DBs:**
  - Place related Python modules in the src/ directory.
  - Follow modular function/class definitions using type hints.
  - Update `main.py` and add argparse parameters if new CLI actions are needed.

- **Testing:**
  - Place pytest-based scripts in `tests/` (if present).
  - Use mock data and coverage checks for critical modules.

- **Logging:**
  - Use the project’s `log` utility for important events and errors.

### Troubleshooting

- **ChromaDB Import Errors:**  
  If you see "cannot import name 'cached_download' from 'huggingface_hub'", run:
  ```sh
  pip install --upgrade sentence-transformers huggingface_hub
  ```
- **Environment Issues:**  
  Double-check .env settings and virtual environment activation.

- **CLI Errors:**  
  Run `python src/main.py --help` to see available commands and parameters.

### Useful Resources

- [ChromaDB documentation](https://docs.trychroma.com/)
- [OpenAI API](https://platform.openai.com/docs/guides/embeddings/use-cases)
- [Sentence Transformers Quick Start](https://www.sbert.net/docs/quickstart.html)

### Contribution
- Use feature branches and submit PRs for review.
- Format code with Black and check PEP8 compliance before committing.
