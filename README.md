# 🚀 Gemini 3 Flash RAG: Production-Grade PDF Intelligence

This project is a high-performance **Retrieval-Augmented Generation (RAG)** system that allows users to ingest PDF documents and perform semantic queries using the **Gemini 3 Flash** ecosystem. Unlike standard tutorials that use lower-resolution vectors, this implementation leverages high-fidelity **3072-dimension embeddings** and event-driven orchestration via **Inngest**.

---

### **🔍 Reliability & Observability (Powered by Inngest)**

One of the core strengths of this project is the use of **Inngest** for background orchestration. Unlike a standard script that simply crashes on error, this system provides:

- **Durable Execution:** Every step (loading, embedding, upserting, inference) is an atomic checkpoint. If the Gemini API hits a rate limit or the database times out, Inngest will automatically retry that specific step without re-running the entire workflow.
- **Live Traces:** Access the **Inngest Dev Server UI** (`http://localhost:8288`) to view a visual timeline of every event. You can inspect the exact data being passed between steps, making debugging vector dimension mismatches or API errors instantaneous.
- **Manual Replays:** If a function fails, you can fix your code and click "Rerun" directly from the Inngest Dashboard. This allows you to resume processing from the failed step without the user needing to re-upload their document.

## 🛠 Tech Stack Details

### **Core AI Engine**

- **LLM Model:** `gemini-3-flash-preview` (Gemini 3 family, Public Preview).
- **Embedding Model:** `models/gemini-embedding-001` (Configured for native **3072 dimensions**).
- **Framework:** `LlamaIndex` (Used for PDF parsing, text chunking, and model interfacing).

### **Infrastructure & Workflow**

- **Orchestration:** [Inngest](https://www.inngest.com/) (Durable execution engine to handle background retries, step functions, and concurrency).
- **Vector Database:** [Qdrant](https://qdrant.tech/) (High-performance vector storage running in Docker).
- **API Framework:** `FastAPI` (Backend serving the Inngest handlers).
- **Frontend UI:** `Streamlit` (Interactive user interface).

---

## 🚀 Setup & Installation

### **1. Prerequisites**

- **Docker Desktop:** Ensure Docker is running on your machine.
- **Python 3.12+:** Recommended to use `uv` for package management.
- **API Access:** A [Google AI Studio](https://aistudio.google.com/) API key.

### **2. Environment Setup**

Create a `.env` file in the root directory:

```env
GOOGLE_API_KEY=your_gemini_api_key_here
```

### **3. Initialize the Vector Database**

Run Qdrant via Docker with local persistence enabled:

```
docker run -p 6333:6333 -p 6334:6334 \
 -v "$(pwd)/qdrant_storage:/qdrant/storage" \
 qdrant/qdrant
```

### **4. Installation**

```
uv sync # Installs Streamlit, FastAPI, Inngest, Qdrant-client, and LlamaIndex

```

### **5. Running the Application**

Open three separate terminal windows:

- **Terminal 1 (Backend):** `uv run uvicorn main:app --reload`

- **Terminal 2 (Inngest Dev):** `npx inngest-cli@latest dev -u http://127.0.0.1:8000/api/inngest`
- **Terminal 3 (Frontend):** `uv run streamlit run streamlit_app.py `


## 📸 Project Results & Visual Evidence

### **1. Functional Streamlit Interface**

![Application Interface](assets/Screenshot 2026-02-12 at 5.44.23 PM.png)

### **2. Query & AI Inference**

![Successful Run](assets/Screenshot 2026-02-12 at 5.46.06 PM.png)


### **3. Real-time Debugging & Error Logs**

![Traceback Analysis](assets/Screenshot 2026-02-12 at 5.44.49 PM.png)

(assets/Screenshot 2026-02-12 at 5.46.30 PM.png)

(assets/Screenshot 2026-02-12 at 5.58.59 PM.png)