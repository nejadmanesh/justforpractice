# backend/main.py
from fastapi import FastAPI
from agents.nerva_agent import build_nerva_agent

app = FastAPI(title="NERVA AI Workspace")
agent = build_nerva_agent()

@app.post("/nerva/run")
async def run_nerva(prompt: str):
    result = agent.run(prompt)
    return {"status": "success", "data": result}
