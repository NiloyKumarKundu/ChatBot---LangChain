
# 🚀 LangChain Chatbot with GROQ Integration

### A Multilingual Translation Chatbot Built with **LangChain** & **GROQ**

This project showcases a powerful chatbot that translates text into different languages using the **LangChain** framework and **ChatGroq** model. With an easy-to-use API built on **FastAPI**, it leverages the performance of **GROQ's** large-scale language models to deliver fast, accurate translations.

---

## 🔧 Project Overview

This chatbot project is built with the following components:

- **FastAPI**: A fast, modern web framework for building APIs.
- **LangChain**: A framework for developing applications powered by large language models (LLMs).
- **GROQ**: A high-performance AI processor used to run the **llama3-8b-8192** model for translations.
- **LangServe**: The platform used to host and run the chatbot.

---

## ⚙️ Features

- **Multilingual Translation**: Translates text into any specified language.
- **API-Driven**: Provides a simple REST API for interacting with the translation service.
- **Seamless Chain of Operations**: Uses LangChain's "Runnable" interface to link together prompts, models, and parsers.
- **Scalable and Flexible**: Easy to extend for other NLP tasks beyond translation.

---

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/langchain-chatbot
cd langchain-chatbot
```

### 2. Set Up the Conda Environment

This project uses **conda** to manage dependencies. Ensure you have conda installed, then create and activate the environment from the `environment.yml` file:

```bash
conda env create -f environment.yml
conda activate langchain-chatbot
```

### 3. Environment Variables

Create a `.env` file and add your API keys:

```bash
LANGCHAIN_API_KEY=your_langchain_api_key
GROQ_API_KEY=your_groq_api_key
```

---

## 🚀 Running the Application

To run the FastAPI server:

```bash
uvicorn app:app --reload --host localhost --port 8000
```

Once the server is up, the chatbot's translation API is accessible at `/chain`.

---

## 🧩 API Endpoints

### 1. Translate Text

#### Request:
- **Endpoint**: `/chain`
- **Method**: `POST`
- **Payload**:
```json
{
  "text": "Hello, how are you?",
  "language": "Spanish"
}
```

#### Response:
```json
{
  "translation": "Hola, ¿cómo estás?"
}
```

---

## 🤖 How It Works

1. **Prompt Creation**: We use **LangChain**'s `ChatPromptTemplate` to create a prompt that asks the model to translate text into the desired language.
2. **Model Integration**: The **ChatGroq llama3-8b** model is used to perform the actual translation.
3. **Parser**: The output from the model is parsed into a simple string format using `StrOutputParser`.
4. **Chain Execution**: The complete process (prompt → model → parser) is linked together using **LangChain’s** "Runnable" interface, and is exposed as an API route using **FastAPI**.

---

## 🙌 Acknowledgments

Big thanks to the teams behind **LangChain**, **GROQ**, and **FastAPI** for their awesome tools that made this project possible!
