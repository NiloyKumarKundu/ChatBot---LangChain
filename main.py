from fastapi import FastAPI, HTTPException
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langserve import add_routes
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
from pydantic import BaseModel

load_dotenv()

# Environment setup
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")


# 1. Create prompt template
system_template = "Translate the following into {language}:"
prompt_template = ChatPromptTemplate.from_messages([
    ('system', system_template),
    ('user', '{text}')
])


# 2. Create model
model = ChatGroq(model="llama3-8b-8192")

# 3. Create parser
parser = StrOutputParser()

# 4. Create chain
chain = prompt_template | model | parser


# 4. App definition
app = FastAPI(
  title="LangChain Server",
  version="1.0",
  description="A simple API server using LangChain's Runnable interfaces",
)

# 5. Adding chain route
add_routes(
    app,
    chain,
    path="/chain",
)


# Define request body structure using Pydantic
class TranslationRequest(BaseModel):
    text: str
    language: str

# Define the /chain endpoint
@app.post("/chain")
async def chain_endpoint(request: TranslationRequest):
    try:
        # Create a dictionary from request data
        request_data = {
            "text": request.text,
            "language": request.language
        }
        # Run the chain with the request data
        result = chain.invoke(request_data)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
