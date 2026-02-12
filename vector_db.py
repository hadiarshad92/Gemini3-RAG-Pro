from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, PointStruct


class QdrantStorage:
    def __init__(self, url="http://localhost:6333", collection="docs", dim=3072):
        self.client = QdrantClient(url=url, timeout=30)
        self.collection = collection
        
        # Check if collection exists and has correct dimensions, create if not
        if not self.client.collection_exists(self.collection):
            self.client.create_collection(
                collection_name=self.collection,
                vectors_config=VectorParams(size=dim, distance=Distance.COSINE),
            )
            
        # else:
        #     # Safety check: Verify existing collection dimensions
        #     info = self.client.get_collection(self.collection)
        #     existing_dim = info.config.params.vectors.size
        #     if existing_dim != dim:
        #         print(f"Warning: Collection {collection} has dim {existing_dim}, but Gemini 3 uses {dim}.")
        #         print("Consider deleting the old collection or using a different collection name.")

    def upsert(self, ids, vectors, payloads):
        points = [PointStruct(id=ids[i], vector=vectors[i], payload=payloads[i]) for i in range(len(ids))]
        # self.client.upsert(self.collection, points=points)
        self.client.upsert(
            collection_name=self.collection,
            points=points,
            wait =True
        ) #new added

    def search(self, query_vector, top_k: int = 5):
        # results = self.client.search(
        results = self.client.query_points(
            collection_name=self.collection,
            # query_vector=query_vector,
            query=query_vector,
            with_payload=True,
            limit=top_k
        ).points  # Add .points at the end to extract the result list, new added
        contexts = []
        sources = set()

        for r in results:
            payload = getattr(r, "payload", None) or {}
            text = payload.get("text", "")
            source = payload.get("source", "")
            if text:
                contexts.append(text)
                sources.add(source)

        return {"contexts": contexts, "sources": list(sources)}