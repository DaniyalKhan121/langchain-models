from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
load_dotenv()   

chat = ChatAnthropic(model ='claude-opus-5', temperature=0.9)

response = chat.invoke("What is the capital of France?")

print(response)