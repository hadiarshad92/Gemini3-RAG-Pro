# from openai import OpenAI
import os
# from llama_index.embeddings.google import GeminiEmbedding
from llama_index.embeddings.google_genai import GoogleGenAIEmbedding
from llama_index.readers.file import PDFReader
from llama_index.core.node_parser import SentenceSplitter
from dotenv import load_dotenv

load_dotenv()

# client = OpenAI()
# EMBED_MODEL = "text-embedding-3-large"
# EMBED_DIM = 3072

EMBED_MODEL_NAME = "models/gemini-embedding-001" 
EMBED_DIM = 3072

# Initialize the Google GenAI Embedding model
# It automatically looks for the GOOGLE_API_KEY environment variable
embed_model = GoogleGenAIEmbedding(model_name=EMBED_MODEL_NAME)

splitter = SentenceSplitter(chunk_size=1000, chunk_overlap=200)

def load_and_chunk_pdf(path: str):
    docs = PDFReader().load_data(file=path)
    texts = [d.text for d in docs if getattr(d, "text", None)]
    chunks = []
    for t in texts:
        chunks.extend(splitter.split_text(t))
    return chunks


# def embed_texts(texts: list[str]) -> list[list[float]]:
#     response = client.embeddings.create(
#         model=EMBED_MODEL,
#         input=texts,
#     )
#     return [item.embedding for item in response.data]

def embed_texts(texts: list[str]) -> list[list[float]]:
    """Converts a list of text chunks into Gemini-3 compatible vector embeddings."""
    # Use the batch embedding method for efficiency
    return embed_model.get_text_embedding_batch(texts)