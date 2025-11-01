from dotenv import load_dotenv
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

# Load environment variables from .env
load_dotenv()

# ✅ Use supported Gemini model for LangChain's v1beta integration
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",  # Fixes the 404 error
    temperature=0.2
)

# Streamlit UI
st.set_page_config(page_title="Research Tool (Gemini Edition)")
st.header("📚 LangChain Models (Gemini Edition)")

# User inputs
paper_input = st.selectbox(
    "Select Research Paper",
    [
        "Attention Is All You Need",
        "BERT: Pre-training of Deep Bidirectional Transformers",
        "GPT-3: Language Models are Few-Shot Learners",
        "Diffusion Models Beat GANs on Image Synthesis"
    ]
)

style_input = st.selectbox(
    "Select Explanation Type",
    ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"]
)

length_input = st.selectbox(
    "Select Explanation Length",
    ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"]
)

# Prompt template
template = PromptTemplate.from_template(
    "Explain the paper '{paper_input}' in a {style_input} style with {length_input} detail."
)

# Run the chain
if st.button("Summarize"):
    chain = template | model
    result = chain.invoke({
        "paper_input": paper_input,
        "style_input": style_input,
        "length_input": length_input
    })
    st.subheader("🧠 Gemini's Explanation")
    st.write(result.content)