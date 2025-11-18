from langchain_community.document_loaders import WebBaseLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
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
    template='Answer the following question - \n {question} from the following text -\n {text}',
    input_variables=['question','text']
)

parser = StrOutputParser()


url = 'https://docs.langchain.com/oss/python/langchain/overview'
loader = WebBaseLoader(url)

docs = loader.load()

chain = prompt | model | parser

result = chain.invoke({'question':'what is langraph?', 'text':docs[0].page_content})
print(result)