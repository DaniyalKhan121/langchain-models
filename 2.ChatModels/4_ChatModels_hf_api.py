import os
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task = "text-generation",
    huggingfacehub_api_token = os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN"),
)

chat = ChatHuggingFace(llm=llm)
response = chat.invoke("what is the capital of pakistan")

print(response.content)