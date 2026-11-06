# Agentic AI

A collection of LLM agents built with **LangChain / LangGraph**: tool-calling agents, retrieval-augmented generation (RAG), memory, structured output, an MCP tool server, and a speech-in / speech-out voice assistant deployed with Streamlit.

Each notebook is a self-contained build of one agent pattern, framed around a realistic enterprise scenario.

## What's inside

| Agent | File | What it shows |
|---|---|---|
| **Enterprise IT Helpdesk Agent** | [`agent_it_helpdesk.ipynb`](agent_it_helpdesk.ipynb) | Tool selection, short-term (thread) memory and long-term memory for an IT support assistant (Wi-Fi, VPN, password resets, ticketing). |
| **Knowledge RAG Agent** | [`agent_knowledge_rag.ipynb`](agent_knowledge_rag.ipynb) | PDF ingestion → chunking → embeddings → **FAISS** vector store → grounded Q&A over a financial-policy document, refusing when the answer isn't in context. |
| **Hospital Assistant (local LLM)** | [`agent_hospital_assistant.ipynb`](agent_hospital_assistant.ipynb) | Fully local RAG with **Ollama** (chat + `nomic-embed-text` embeddings) and **Chroma**, wrapped as a tool for an agent with an in-memory checkpointer. |
| **R&D Literature Research Agent** | [`agent_literature_research.ipynb`](agent_literature_research.ipynb) | Tool-calling agent over **Wikipedia** and **PubMed** that returns a typed `ResearchBrief` via Pydantic structured output. |
| **Enterprise Knowledge & Data Assistant** | [`retriver.ipynb`](retriver.ipynb) | One agent, three sources: internal docs (Chroma + MiniLM embeddings), Wikipedia, and a **SQL agent** over a SQLite database. |
| **MCP tool server + client** | [`mcp/`](mcp) | A Model Context Protocol server exposing student-record tools, and a LangChain agent that discovers and calls them over HTTP. |
| **Medical Voice Assistant** | [`project_2/`](project_2) | Speech → **faster-whisper** transcription → tool-calling LLM grounded on **MedlinePlus** → **edge-tts** speech. Shipped as a Streamlit app ([`app.py`](project_2/app.py)) with safety rules (no diagnosis, no prescriptions). |

## Stack

Python · LangChain · LangGraph · OpenRouter · Ollama · FAISS · Chroma · HuggingFace sentence-transformers · MCP · faster-whisper · edge-tts · Streamlit · SQLite

## Getting started

```bash
git clone https://github.com/Diyaaa-12/Agentic_AI.git
cd Agentic_AI
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
cp .env.example .env                                # then add your OPENROUTER_API_KEY
```

**Notebooks:** open any `.ipynb` in Jupyter / VS Code; the first cell installs what it needs. The hospital assistant needs [Ollama](https://ollama.com) running locally.

**Voice assistant (Streamlit):**

```bash
pip install -r project_2/requirements.txt
streamlit run project_2/app.py
```

**MCP demo:**

```bash
pip install -r mcp/requirements.txt
python mcp/s.py     # start the MCP server on :8000
python mcp/c.py     # agent discovers and calls the server's tools
```

## Notes

- API keys are read from `.env` (never committed); see [`.env.example`](.env.example).
- The medical assistant gives general educational information only. It is not a diagnostic tool.
