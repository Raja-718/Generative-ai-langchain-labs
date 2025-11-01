from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import google.generativeai as genai
import os

# Load environment variables
load_dotenv()

# Set Gemini API key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

# Initialize Gemini model
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")  # or "gemini-1.5-flash" if supported

# Message history
messages = [
    SystemMessage(content="You are a helpful assistant"),
    HumanMessage(content="Tell me about Langchain")
]

# Invoke Gemini model
result = model.invoke(messages)

# Append AI response
messages.append(AIMessage(content=result.content))

# Print conversation
for msg in messages:
    print(f"{msg.type}: {msg.content}")