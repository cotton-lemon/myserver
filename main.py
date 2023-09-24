from fastapi import FastAPI
from getcode import getcode
from Crypto.PublicKey import RSA 
import asyncio
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import time
app = FastAPI()
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "https://auth.dgist.ac.kr",
    'http://auth.dgist.ac.kr'
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class codeParam(BaseModel):
    id: str
    pw: str

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/code")
async def root(param:codeParam):
    start=time.time()
    a=getcode(param.id,param.pw)
    code=await a;
    print(f"time: {time.time()-start}")
    return {"code": code}