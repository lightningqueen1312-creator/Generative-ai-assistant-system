 Enterprise AI Knowledge Assistant

An industry-ready **Retrieval-Augmented Generation (RAG)** application that allows users to upload enterprise PDF documents and ask natural language questions using **Gemini 2.5 Flash**.

The application retrieves relevant information from uploaded documents using **Sentence Transformers** and **FAISS**, then generates accurate answers with **Google Gemini**.


Features

-  Upload PDF documents
-  Intelligent document chunking
-  Sentence Transformer embeddings
-  FAISS vector similarity search
-  Gemini 2.5 Flash integration
-  ChatGPT-style conversation interface
-  Conversation memory
-  Retrieved context (RAG explainability)
-  Chat history
-  Download chat history
-  Dashboard metrics
-  Error handling
-  Streamlit web interface

 Tech Stack

- Python 3.13
- Streamlit
- LangChain 1.3.x
- Google Gemini 2.5 Flash
- Sentence Transformers
- FAISS
- SQLite
- Prompt Engineering


 Project Structure


Enterprise-AI-Knowledge-Assistant/
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── database/
│   └── database.py
│
├── prompts/
│   └── prompt_templates.py
│
├── utils/
│   ├── pdf_reader.py
│   ├── chunking.py
│   ├── embeddings.py
│   ├── vectorstore.py
│   ├── llm.py
│   ├── memory.py
│
├── uploads/
├── vector_db/
├── chat_history/
└── assets/


 Installation

Clone the repository


git clone <repository-url>
cd Enterprise-AI-Knowledge-Assistant


 Create a virtual environment

 Windows

python -m venv venv
venv\Scripts\activate


 Install dependencies

python -m pip install --upgrade pip

pip install streamlit langchain==1.3.11 langchain-core langchain-google-genai google-generativeai sentence-transformers faiss-cpu numpy pypdf python-dotenv pandas tqdm

 Configure Environment Variables

Create a `.env` file in the project root.

Example:

GOOGLE_API_KEY=your_google_api_key



 Run the Application


streamlit run app.py


The application will open automatically in your browser.


 Workflow

1. Upload a PDF document.
2. The document is read and split into chunks.
3. Sentence Transformers generate embeddings.
4. FAISS stores the embeddings.
5. Ask a question in natural language.
6. Relevant document chunks are retrieved.
7. Gemini 2.5 Flash generates an answer using the retrieved context.
8. The answer and chat history are displayed.


 Example Questions

- Summarize this document.
- What is the leave policy?
- Explain the employee benefits.
- What are the responsibilities of HR?
- List the important points.

 Future Enhancements

- Multi-document support
- User authentication
- Role-based access
- Hybrid search (BM25 + FAISS)
- Conversation export (PDF)
- Cloud database integration
- Admin dashboard
- Speech-to-text input



Author

Krithika S

Enterprise AI Knowledge Assistant

Built using Python, Streamlit, LangChain, FAISS, Sentence Transformers, and Google Gemini.