from os import getenv
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()
url = getenv('DATABASE_URL')

engine = create_async_engine(url)
session = sessionmaker(engine, class_=AsyncSession)
