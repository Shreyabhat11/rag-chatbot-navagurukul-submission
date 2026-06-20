import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

sys.path.append(str(ROOT_DIR))
import streamlit as st

from rag.pipeline import RAGPipeline
from vectordb.qdrant_manager import QdrantManager


st.set_page_config(
    page_title="System Design RAG",
    layout="wide"
)

# Load pipeline once
@st.cache_resource
def load_pipeline():

    return RAGPipeline()


pipeline = load_pipeline()


# Sidebar
with st.sidebar:

    st.title("📚 Knowledge Base")

    qdrant = QdrantManager()

    try:
        total_chunks = qdrant.count()
    except:
        total_chunks = "N/A"

    st.metric(
        "PDFs",
        46
    )

    st.metric(
        "Indexed Chunks",
        total_chunks
    )

    st.markdown("---")

    st.write("Vector DB: Qdrant")

    st.write("Embedding: BGE Small")

    st.write("LLM: Groq")

    st.markdown("---")

    st.info(
        "System Design Knowledge Assistant"
    )


# Main page
st.title(
    "🚀 System Design RAG Assistant"
)

st.markdown(
    """
Ask questions across all your
System Design books.
"""
)


# Chat history
if "messages" not in st.session_state:

    st.session_state.messages = []


# Display old messages
for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):

        st.markdown(
            message["content"]
        )


# User input
query = st.chat_input(
    "Ask something..."
)


if query:

    # Show user msg
    st.session_state.messages.append(
        {
            "role": "user",
            "content": query
        }
    )

    with st.chat_message("user"):

        st.markdown(query)

    # Generate answer
    with st.spinner(
        "Searching books..."
    ):

        result = pipeline.ask(
            query
        )

    answer = result["answer"]

    # Assistant msg
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )
    st.metric(
        "Latency",
        f"{result['latency']:.2f}s"
    )

    with st.chat_message(
        "assistant"
    ):

        st.markdown(answer)

        st.markdown("---")

        st.subheader(
            "📖 Sources"
        )

        for source in result[
            "sources"
        ]:

            st.info(
                f"""
PDF:
{source['pdf_name']}

Page:
{source['page_number']}
"""
            )

        st.subheader(
            "⚡ Metrics"
        )

        st.metric(
            "Latency",
            f"{result['latency']:.2f}s"
        )

        st.metric(
            "Retrieved Chunks",
            len(
                result["sources"]
            )
        )

        st.markdown("---")

        st.subheader(
            "🔍 Retrieved Chunks"
        )

        for i, chunk in enumerate(
            result["sources"],
            start=1
        ):

            with st.expander(
                f"Chunk {i}"
            ):

                st.write(
                    chunk["text"][:1500]
                )