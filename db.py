from os import getenv
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

url = getenv('DB_URL')

engine = create_async_engine(url)
session = sessionmaker(engine, Class=AsyncSession)