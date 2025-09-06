🤖 **Chatbot with LangChain, Streamlit & LLMs**

This project demonstrates how to build a chatbot using LangChain, Streamlit, and different LLMs (OpenAI GPT & Ollama LLaMA2).
You can switch between models depending on your use case! 🚀

✨ **Features**

🧩 Modular design using LangChain chains

💬 Chat interface with Streamlit

🔑 Supports both OpenAI GPT-3.5 and Ollama LLaMA2

📊 Integrated with LangSmith tracing for monitoring

1️⃣ **Install Dependencies**

pip install -r requirements.txt

2️⃣ **Add Environment Variables**

Create a file named .env in the project root and add:

OPENAI_API_KEY=your_openai_api_key

LANGCHAIN_API_KEY=your_langchain_api_key

LANGSMITH_ENDPOINT=https://api.smith.langchain.com

PROJECT_NAME=ChatbotProject

👉 **If you’re using Ollama, make sure it’s installed**

▶️ **Running the Chatbots**

🔹 OpenAI GPT-3.5

streamlit run app_openai.py

🔹 **Ollama LLaMA2**

streamlit run app_ollama.py
