from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
chat = ChatGoogleGenerativeAI(model="gemini-3.6-flash", temperature=0.9)
response = chat.invoke("What is the capital of France?")  

print(response)