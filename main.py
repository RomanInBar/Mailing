import os

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi.middleware.cors import CORSMiddleware
from redis import asyncio as aioredis

from client.routers import router as client_router
from database.engine import Base
from mailing.routers import router as mailing_router

load_dotenv('.env')
app = FastAPI(title="Mailing")
app.include_router(client_router)
app.include_router(mailing_router)

REDIS_HOST = os.getenv('REDIS_HOST')
REDIS_PORT = os.getenv('REDIS_PORT')

origins = [
    'http://127.0.0.1:8080',
    'http://localhost:8080'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['GET', 'POST', 'PATCH', 'DELETE'],
    allow_headers=['*']
)


@app.on_event("startup")
async def startup_event():
    redis = aioredis.Redis(
        host=REDIS_HOST,
        port=REDIS_PORT,
        encoding="utf-8",
        decode_responses=True,
    )
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
