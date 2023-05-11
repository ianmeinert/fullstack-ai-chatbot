import os
import redis

from dotenv import load_dotenv

load_dotenv()

AZ_REDIS_KEY = os.getenv('AZ_REDIS_KEY')
AZ_REDIS_HOST = os.getenv('AZ_REDIS_HOST')
AZ_REDIS_PORT = os.getenv('AZ_REDIS_PORT')

r = redis.StrictRedis(host=AZ_REDIS_HOST, port=AZ_REDIS_PORT, db=0, password=AZ_REDIS_KEY, ssl=True)

r.set('foo', 'bar')
result = r.get('foo')

print(result)