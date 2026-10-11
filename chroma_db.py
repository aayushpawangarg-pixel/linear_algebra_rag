
import chromadb
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Paths
data_path = r"data"
chroma_path = r"chroma_db"

# Initialize ChromaDB with persistent storage
chroma_client = chromadb.PersistentClient(path=chroma_path)

# Create or access the collection
collection = chroma_client.get_or_create_collection(
    name="Linear-Algebra-Notes"
)

loader = PyPDFDirectoryLoader(data_path)
documents = loader.load()

print(f"Loaded {len(documents)} pages from PDF files.")

# Split documents into smaller chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100,
    length_function=len,
    is_separator_regex=False
)

chunks = text_splitter.split_documents(documents)

print(f"Created {len(chunks)} text chunks.")

ids = [f"ID{i}" for i in range(len(chunks))]

collection.upsert(
    documents=[chunk.page_content for chunk in chunks],
    metadatas=[chunk.metadata for chunk in chunks],
    ids=ids
)

print(f"Stored {len(chunks)} chunks in ChromaDB.")
print(f"Total chunks in collection: {collection.count()}")
