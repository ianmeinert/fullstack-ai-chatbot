import os
import redis
from urllib.parse import quote

from dotenv import load_dotenv
from rejson import Client

load_dotenv()


class Redis:
    def __init__(self):
        """initialize  connection """
        self.redisJson = None
        self.connection = None
        self.REDIS_USER = quote(os.environ['REDIS_USER'])
        self.REDIS_PASSWORD = quote(os.environ['REDIS_PASSWORD'])
        self.REDIS_HOST = quote(os.environ['REDIS_HOST'])
        self.REDIS_PORT = quote(os.environ['REDIS_PORT'])
        self.connection_url = f"redis://{self.REDIS_USER}:{self.REDIS_PASSWORD}@{self.REDIS_HOST}:{self.REDIS_PORT}"

    async def create_connection(self):
        self.connection = redis.from_url(
            self.connection_url, db=0)
        return self.connection

    def create_rejson_connection(self):
        self.redisJson = Client(host=self.REDIS_HOST,
                                port=self.REDIS_PORT,
                                decode_responses=True,
                                username=self.REDIS_USER,
                                password=self.REDIS_PASSWORD)

        return self.redisJson
