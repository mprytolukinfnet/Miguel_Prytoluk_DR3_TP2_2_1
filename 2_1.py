from fastapi import FastAPI
from pydantic import BaseModel
from langchain_core.language_models.fake import FakeListLLM

# Inicialização do FastAPI
app = FastAPI()

# Modelo de entrada
class TextInput(BaseModel):
    query: str

# Configuração do Fake LLM
responses = [
    "Fico muito feliz com a sua pergunta, mas sou apenas um modelo de teste.",
    "Não tenho capacidade de responder sua pergunta especificamente.",
]
fake_llm = FakeListLLM(responses=responses)

@app.post("/chat/")
async def chat(input: TextInput):
    response = fake_llm(input.query)
    return {"query": input.query, "response": response}

'''
Executar com
curl -X POST "http://127.0.0.1:8000/chat/" \
-H "Content-Type: application/json" \
-d '{"query": "Qual a capital da França?"}'
'''