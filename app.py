import streamlit as st
from faq_data import faq_data
from rapidfuzz import process

st.set_page_config(
    page_title="AI FAQ Chatbot",
    page_icon="🤖",
    layout="wide"
)

st.sidebar.title("🤖 AI FAQ Chatbot")

st.sidebar.info(
    """
    Features

    ✅ NLP-based Question Matching
    ✅ FAQ Knowledge Base
    ✅ Fast Response
    ✅ Streamlit UI
    """
)

st.title("🤖 AI FAQ Chatbot")

st.markdown(
    "Ask questions related to Artificial Intelligence and Technology."
)

question = st.text_input(
    "Enter your question"
)

if st.button("Ask"):

    if question.strip():

        match = process.extractOne(
            question.lower(),
            faq_data.keys()
        )

        if match and match[1] > 60:

            answer = faq_data[match[0]]

            st.success(answer)

            st.caption(
                f"Matched Question: {match[0]}"
            )

        else:

            st.error(
                "Sorry, I couldn't find a suitable answer."
            )

st.markdown("---")

st.subheader("📚 Available Questions")

for item in faq_data.keys():
    st.write("•", item.title())

st.markdown("---")

st.markdown(
    "Made with ❤️ using Python, Streamlit and NLP Matching"
)