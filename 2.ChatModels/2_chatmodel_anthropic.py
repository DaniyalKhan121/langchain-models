from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
load_dotenv()   

chat = ChatAnthropic(model='claude-sonnet-4-20250514', temperature=0.9)

response = chat.invoke("What is the capital of France?")

print(response)