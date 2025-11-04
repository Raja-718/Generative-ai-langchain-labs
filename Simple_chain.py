from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
load_dotenv()

prompt = PromptTemplate(
    template='Generate 5 interesting facts about {topic}',
    input_variables=['topic']
)

# Load environment variables
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# Initialize Gemini Flash 2.0
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",  # Use "gemini-1.5-pro" if needed
    google_api_key=api_key
)

parser = StrOutputParser()

chain = prompt | llm | parser

result = chain.invoke({'topic':'cricket'})

print(result)

chain.get_graph().print_ascii()