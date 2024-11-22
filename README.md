# TP2 Exercício 2_1: Chatbot Simulado com Fake LLM
Simulação de chatbot utilizando LangChain e Fake LLM para responder a entradas pré-definidas.

**Passos para Configuração**:

1. Certifique-se de que o ambiente Python está configurado.
2. Instale as dependências necessárias:
```bash
pip install -r requirements.txt
```

**Como Executar**: Inicie o servidor FastAPI com o comando:
```bash
uvicorn 2_1:app --reload
```

**Uso da API**: Envie uma pergunta para o chatbot:

```bash
curl -X POST "http://127.0.0.1:8000/chat/" \
-H "Content-Type: application/json" \
-d '{"query": "Qual a capital da França?"}'
```