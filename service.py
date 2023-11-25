from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer
from qdrant_client.models import Filter
from fastapi import FastAPI
import uvicorn
from NEURAL_SEARCH import NeuralSearcher


app = FastAPI()
collection_name="Promit_BIGBasket_CHAABI"

# Creating an instance for Neural Searcher
neural_searcher = NeuralSearcher(collection_name=collection_name)

@app.get("/api/search")
async def search_startup(q: str):
    summary,payload=neural_searcher.search(text=q)
    return {
        "result": payload,
        "summary":summary
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8085)



