from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np  

load_dotenv()

embedding = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=300)

docoments = [
    "Shahid Afridi: Boom Boom, All-rounder, Six-hitter, Aggressive, Legend",
    "Babar Azam: Batsman, Cover Drive, Classy, Captain, Run Scorer",
    "Imran Khan: Former Captain, All-rounder, Leg-spinner",
    "Saeed Anwar: Batsman, Aggressive, Left-handed",
    "Inzamam-ul-Haq: Batsman, Captain, Right-handed"
]

query = "tell me about Babar Azam"

doc_embeddings = embedding.embed_documents(docoments)

query_embedding = embedding.embed_query(query)

scores = cosine_similarity([query_embedding], doc_embeddings)

index, score = sorted(list(enumerate(scores)),key=lambda x: x[1], reverse=True)[-1]

print(query)
print(docoments[index])
print("similarity score is : ", score)