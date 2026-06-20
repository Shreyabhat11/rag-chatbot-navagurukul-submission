import streamlit as st


def render_source_card(source):

    st.info(
        f"""
📄 {source['pdf_name']}

📖 Page {source['page_number']}
"""
    )


def render_chunk(chunk):

    with st.expander(
        f"{chunk['pdf_name']} "
        f"(Page {chunk['page_number']})"
    ):
        st.write(
            chunk["text"][:2000]
        )