from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_google_genai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

messages = [
    SystemMessage(content="You are a helpful assistant"),
    HumanMessage(content="Tell me about Langchain")
]

result = model.invoke(messages)

messages.append(AIMessage(content = result.content))

print(messages)

