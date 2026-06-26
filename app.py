import streamlit as st

# ============================
# Database
# ============================
from database.database import save_chat

# ============================
# PDF Processing
# ============================
from utils.pdf_reader import read_pdf
from utils.chunking import split_text
from utils.embeddings import (
    create_embeddings,
    embed_query
)
from utils.vectorstore import (
    save_vector_store,
    search_similar_chunks
)

# ============================
# Prompt Engineering
# ============================
from prompts.prompt_templates import get_prompt

# ============================
# Gemini
# ============================
from utils.llm import generate_answer

# ============================
# Memory
# ============================
from utils.memory import ChatMemory

# ============================
# Page Configuration
# ============================

st.set_page_config(
    page_title="Enterprise AI Knowledge Assistant",
    page_icon="🤖",
    layout="wide"
)

# ============================
# Session State
# ============================

if "memory" not in st.session_state:
    st.session_state.memory = ChatMemory()

if "messages" not in st.session_state:
    st.session_state.messages = []

if "document_uploaded" not in st.session_state:
    st.session_state.document_uploaded = False

# ============================
# Main Heading
# ============================

st.title("🤖 Enterprise AI Knowledge Assistant")

st.caption(
    "Industry-Ready Retrieval-Augmented Generation (RAG) Assistant using Gemini 2.5 Flash"
)

st.divider()
# =====================================================
# SIDEBAR
# =====================================================

with st.sidebar:

    st.header("📄 Upload Document")

    uploaded_file = st.file_uploader(
        "Upload PDF Document",
        type=["pdf"]
    )

    st.divider()

    st.header("⚙ Prompt Engineering")

    prompt_type = st.selectbox(
        "Prompt Technique",
        (
            "Role Prompt",
            "Chain of Thought",
            "Few Shot",
            "Zero Shot"
        )
    )

    st.divider()

    st.header("📊 System Status")

    if st.session_state.document_uploaded:
        st.success("✅ Document Loaded")
    else:
        st.warning("⚠ No document uploaded")

    st.divider()

    # Define the button here
    clear_chat = st.button(
        "🗑 Clear Chat",
        use_container_width=True
    )

    if clear_chat:
     st.session_state.memory.clear()
     st.session_state.messages = []
     st.session_state.document_uploaded = False
     st.rerun()
        # =====================================================
# DASHBOARD METRICS
# =====================================================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Messages",
        len(st.session_state.messages)
    )

with col2:
    st.metric(
        "Document",
        "Loaded" if st.session_state.document_uploaded else "Not Loaded"
    )

with col3:
    st.metric(
        "AI Model",
        "Gemini 2.5 Flash"
    )

st.divider()
        # =====================================================
# PDF PROCESSING
# =====================================================

if uploaded_file is not None:

    try:

        with st.spinner("📄 Processing document..."):

            # Read PDF
            document_text = read_pdf(uploaded_file)

            # Split into chunks
            chunks = split_text(document_text)

            # Create embeddings
            embeddings = create_embeddings(chunks)

            # Save FAISS Vector Store
            save_vector_store(
                embeddings,
                chunks
            )

            st.session_state.document_uploaded = True

        st.success("✅ PDF processed successfully!")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Chunks Created",
                len(chunks)
            )

        with col2:
            st.metric(
                "Embedding Vectors",
                len(embeddings)
            )

    except Exception as e:

        st.error("❌ Failed to process the PDF.")

        st.exception(e)
        # =====================================================
# CHAT HISTORY DISPLAY
# =====================================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        # =====================================================
# CHAT INPUT
# =====================================================

question = st.chat_input(
    "Ask a question about your document..."
)
if question:

    # -------------------------
    # Save User Message
    # -------------------------

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    # -------------------------
    # Check PDF
    # -------------------------

    if not st.session_state.document_uploaded:

        with st.chat_message("assistant"):

            st.warning("Please upload a PDF first.")

    else:

        try:

            with st.spinner("🤖 Thinking..."):

                # Query Embedding
                query_embedding = embed_query(question)

                # Retrieve Similar Chunks
                relevant_chunks = search_similar_chunks(
                    query_embedding
                )

                # Context
                context = "\n\n".join(relevant_chunks)

                # Prompt
                prompt = get_prompt(
                    context=context,
                    question=question,
                    prompt_type=prompt_type
                )

                # Gemini Response
                answer = generate_answer(prompt)

                # Save Database
                save_chat(question, answer)

                # Save Memory
                st.session_state.memory.add(
                    question,
                    answer
                )

            # -------------------------
            # Save Assistant Message
            # -------------------------

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": answer
                }
            )

            with st.chat_message("assistant"):

                st.markdown(answer)

                with st.expander("📚 Retrieved Context"):

                    if relevant_chunks:

                        for i, chunk in enumerate(relevant_chunks):

                            st.markdown(
                                f"### Chunk {i+1}"
                            )

                            st.write(chunk)

                    else:

                        st.warning(
                            "No relevant chunks found."
                        )

        except Exception as e:

            st.error(
                "Error while generating answer."
            )

            st.exception(e)
            # =====================================================
# DOWNLOAD CHAT HISTORY
# =====================================================

if st.session_state.messages:

    chat_text = ""

    for msg in st.session_state.messages:

        role = msg["role"].capitalize()

        chat_text += f"{role}: {msg['content']}\n\n"

    st.download_button(
        label="📥 Download Chat History",
        data=chat_text,
        file_name="chat_history.txt",
        mime="text/plain"
    )
    # =====================================================
# EMPTY STATE
# =====================================================

if not st.session_state.messages:

    st.info(
        """
👋 Welcome!

Upload an enterprise PDF and start asking questions.

Examples:

• Summarize this document

• Explain the leave policy

• What are the responsibilities of HR?

• Give me important points
"""
    )