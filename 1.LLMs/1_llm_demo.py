from langchain_openai import OpenAI
from dotenv import load_dotenv
load_dotenv()  

llm = OpenAI(model_name="gpt-4o", temperature=0.9)
 
response = llm.invoke("What would be a good company name for a company that makes colorful socks?")

print(response)