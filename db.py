from os import getenv
from sqlalchemy.ext.asyncio import asynSession, create_async_engine

url = getenv('DB_URL')
engine = create_async_engine(url)