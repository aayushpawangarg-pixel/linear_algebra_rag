import chromadb
from google import genai
from dotenv import load_dotenv

load_dotenv()

data_path = r"data"
chroma_path = r"chroma_db"

chroma_client = chromadb.PersistentClient(path=chroma_path)

collection = chroma_client.get_or_create_collection(name="Linear-Algebra-Notes")

user_query = input("Enter your query: \n\n")

results = collection.query(
    query_texts=[user_query],
    n_results=1
)

client = genai.Client()

system_prompt = """You are a helpful assistant that provides concise and accurate answers based on the provided context. If the context does not contain enough information to answer the question, respond with 'I don't know.
The data:
"""+str(results['documents']) + """ 
"""+str(results['metadatas']) + """
'"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=system_prompt + "\n\nUser question: " + user_query
)

print("\n\n   RESPONSE  \n")
print(response.text)

