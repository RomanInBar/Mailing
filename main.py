from fastapi import FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis import asyncio as aioredis

from client.routers import router as client_router
from mailing.routers import router as mailing_router
from database.engine import Base


app = FastAPI(
    title='Mailing'
)
app.include_router(client_router)
app.include_router(mailing_router)


@app.on_event('startup')
async def startup_event():
    redis = aioredis.from_url('redis://localhost:6379/0', encoding='utf-8', decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix='fastapi-cache')
