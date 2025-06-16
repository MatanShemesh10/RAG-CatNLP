![CatNLP-logo](https://github.com/user-attachments/assets/f60ff8fd-c8a8-4188-9098-ed7770ea6fbf)

# 🐱 CatNLP – Local RAG Chatbot

CatNLP is a local Retrieval-Augmented Generation (RAG) chatbot that runs fully offline on your machine. It was built using [this guide by ngxson](https://huggingface.co/blog/ngxson/make-your-own-rag) and uses a customized frontend forked and modified from [LocalLLMChat](https://github.com/dmeldrum6/LocalLLMChat).

---

## 🚀 What This Project Does
This chatbot can answer questions based on a custom document you provide. It uses a local embedding model to understand your document and a local language model (via [Ollama](https://ollama.com/)) to generate human-like answers grounded in your content.

The goal: create a private, efficient chatbot that gives answers based strictly on your data — without relying on any cloud API.

## Usage Example:

![example-chat](https://github.com/user-attachments/assets/a7bd801b-d4b4-43a5-b574-d0d879dce4ed)


---

## 🧠 How It Works (RAG Overview)

We use a standard **RAG (Retrieval-Augmented Generation)** pipeline:

1. **Embedding Phase (Preprocessing):**
   - A local document (e.g. a text file with facts) is split into chunks (in our case: per line).
   - Each chunk is converted into a numerical vector using an **embedding model**.

2. **Retrieval Phase (at runtime):**
   - When a user asks a question, we compute its embedding.
   - We compare this to the precomputed vectors and find the top-N most similar chunks (via cosine similarity).

3. **Generation Phase:**
   - These relevant chunks are passed to the **language model** as context.
   - The model generates a final response based only on those chunks.

---

## 🔍 Models Used
- **Embedding Model:** `CompendiumLabs/bge-base-en-v1.5-gguf`
  - Used to convert text into dense vectors (for similarity search).

- **Language Model:** `bartowski/Llama-3.2-1B-Instruct-GGUF`
  - A small LLM run locally via Ollama, used to generate the final answer.

---

## 💡 The Input Document
We used a sample `.txt` file containing factual knowledge (e.g. about cats). The file is embedded once during startup and stored in memory as vector representations. 

> You can replace it with any custom file by modifying `main.py` to load your own text.

---

## 🖥️ Frontend (LocalLLMChat Custom)
The frontend is based on `LocalLLMChat`, modified to:
- Use our `/chat` endpoint instead of OpenAI’s format.
- Send only a plain `query` instead of structured `messages`.
- Display the full assistant answer along with debug info if needed.

The UI is lightweight, works from a local file, and does not require a webserver.

---

## 🛠️ How To Run Locally

### 1. Prerequisites
- Python 3.9+
- [Ollama](https://ollama.com) installed and running
- pip

### 2. Install dependencies
```bash
pip install flask flask-cors numpy
```

### 3. Run the server
```bash
python main.py
```
By default, it runs on `http://localhost:5000/chat`

### 4. Open the frontend
Open `LocalLLMChatv2.html` directly in your browser (double-click or drag into tab).

---

## 📂 Project Structure
```
├── main.py               # Flask server with RAG pipeline
├── main_model.py         # Original CLI script for reference
├── LocalLLMChatv2.html   # Custom frontend
├── cat-facts.txt         # Input document to embed
```

---

## 🐾 Logo & Branding
The chatbot is named **CatNLP** — a play on "cat" and "NLP" (natural language processing). It features a custom robotic-cat themed logo.

---

## 🔒 Offline & Private
All processing is local. No API keys, no internet needed.
Perfect for building private chatbots on your own knowledge base.

---

## 📌 Inspired by
- [Make Your Own RAG](https://huggingface.co/blog/ngxson/make-your-own-rag)
- [LocalLLMChat](https://github.com/dmeldrum6/LocalLLMChat)
