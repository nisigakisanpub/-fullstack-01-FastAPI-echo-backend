from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import asyncio

app = FastAPI()

#CORS設定(Next.jsとの通信を許可)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/echo")
async def echo (request: Request):
    data = await request.json()
    message = data.get("message", "")
    await asyncio.sleep(3) #1秒待機
    return {"echo": message}

