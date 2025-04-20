import redis
from redis.cache import CacheConfig
import json
from dotenv import load_dotenv
import os

load_dotenv()

def cache_connection():
    return redis.Redis(
        host=os.getenv('REDIS_HOST'),
        port=os.getenv('REDIS_PORT'),
        protocol=3,
        cache_config=CacheConfig(),
        decode_responses=True,
        username=os.getenv('REDIS_USER'),
        password=os.getenv('REDIS_PASSWORD'),
    )

    
def check_cached(r, cached_key):
    cached_data = r.get(cached_key)

    if cached_data:
        return json.loads(cached_data)
    else:
        return None
    
def create_cache(r, cache_key , cache_data, exp_time):
    r.setex(cache_key, exp_time, json.dumps(cache_data))