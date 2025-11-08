from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence
import os

# Load environment variables
load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")

# Initialize Gemini Flash 2.5
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=google_api_key
)

prompt = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)
parser = StrOutputParser()

prompt2 = PromptTemplate(
    template='Explain the following joke {text}',
    input_variables=['text']
)

chain = RunnableSequence(prompt, model, parser, prompt2, model, parser)

print(chain.invoke({'topic':'AI'}))