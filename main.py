import chromadb
from google import genai
from dotenv import load_dotenv

load_dotenv()

data_path = r"data"
chroma_path = r"chroma_db"

chroma_client = chromadb.PersistentClient(path=chroma_path)

collection = chroma_client.get_or_create_collection(name="Linear-Algebra-Notes")

user_query = input("Enter your query: ")

results = collection.query(
    query_texts=[user_query],
    n_results=3
)
print("\n--- RETRIEVED CHUNKS ---\n")

for i, document in enumerate(results["documents"][0], start=1):
    print(f"\nCHUNK {i}:\n")
    print(document)

client = genai.Client()

system_prompt = """You are a helpful assistant that provides concise and accurate answers based on the provided context. If the context does not contain enough information to answer the question, respond with 'I don't know.
The data:
"""+str(results['documents']) + """ 
"""+str(results['metadatas']) + """
'"""

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=system_prompt + "\n\nUser question: " + user_query
)

print("\nRESPONSE\n")
print(response.text)
