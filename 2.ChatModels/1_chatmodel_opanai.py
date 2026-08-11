from  langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()   

chat = ChatOpenAI(model_name="gpt-5.6-sol", temperature=0.9)

response = chat.invoke("What would be a good company name for a company that makes colorful socks?")

print(response)