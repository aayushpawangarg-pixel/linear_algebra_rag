# Linear Algebra RAG 📚

A simple RAG-based study assistant that helps answer questions from Linear Algebra PDF notes using Google Gemini and ChromaDB.

## 💡 About the Project

While studying Linear Algebra, I wanted to explore how AI could help me find answers from my study material instead of manually searching through lengthy PDFs.

So, I built this project to understand how **Retrieval-Augmented Generation (RAG)** works in practice.

The idea is simple: ask a question, retrieve the most relevant parts of the notes, and let Gemini generate an answer using that context.

## ⚙️ How It Works

Here's what happens when you ask a question:

1. **Load the PDFs:** Extract text from Linear Algebra notes.
2. **Split the text:** Break the content into smaller chunks so it's easier to search.
3. **Store the chunks:** Save the processed text in ChromaDB for later retrieval.
4. **Retrieve relevant content:** Find the three most relevant chunks for your question.
5. **Generate an answer:** Pass the retrieved content to Google Gemini, which uses it to answer your question.

## ✨ Features

- Ask questions about Linear Algebra notes.
- Process PDF files and split their content into manageable chunks.
- Store document chunks in a persistent ChromaDB database.
- Generate answers using Google Gemini.
- Avoid answering unrelated questions when the retrieved notes don't provide the required information.

## 🛠️ Built With

- **Python** — Project logic
- **Google Gemini** — Generating answers
- **ChromaDB** — Storing and retrieving document chunks
- **LangChain Text Splitters** — Splitting text into chunks
- **PyPDF** — Extracting text from PDFs
- **python-dotenv** — Managing environment variables

## 📁 Project Structure

```text
linear_algebra_rag/
├── data/              # Linear Algebra PDF notes
├── chroma_db/         # Local vector database
├── chroma_db.py       # PDF processing and database creation
├── main.py            # Question answering logic
├── requirements.txt   # Project dependencies
├── .env               # Gemini API key (not committed)
├── .gitignore
└── README.md
```

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/aayushpawangarg-pixel/linear_algebra_rag.git
cd linear_algebra_rag
```

### 2. Create a virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install the dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up your API key

Create a `.env` file in the project folder and add your Google Gemini API key:

```env
GEMINI_API_KEY=your_api_key_here
```

Keep your actual API key private. Don't upload your `.env` file to GitHub.

### 5. Add your notes

Create a `data` folder and place your Linear Algebra PDF notes inside it.

### 6. Process the PDFs

```bash
python chroma_db.py
```

This extracts the text, splits it into chunks, and stores the content in ChromaDB.

### 7. Start asking questions

```bash
python main.py
```

Enter a question about Linear Algebra and see the answer generated from your notes.

## 🔭 What's Next?

There are still things I'd like to improve:

- Add a Streamlit interface to make the project easier to use.
- Show which pages or sections were used to generate an answer.
- Improve retrieval so that answers are more accurate.
- Support multiple subjects and document collections.

## 🎯 What I'm Learning

Through this project, I'm getting hands-on experience with RAG pipelines, vector databases, document chunking, information retrieval, and integrating LLMs into Python applications.

This is a learning project, and I'll keep improving it as I learn more about AI and RAG.

---

*Built as part of my journey into AI and LLM-based applications.*