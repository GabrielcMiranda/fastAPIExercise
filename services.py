from models import User
from connection import session
from sqlalchemy import delete

class UserService:
    async def create_user(name):
        async with session() as session:
            session.add(User(name=name))
            await session.commit()

    async def delete_user(id):
        async with session() as session():
            await session.execute(delete(User).where(User.id == id))
            await session.commit()
