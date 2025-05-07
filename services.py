from models import User
from connection import session

class UserService:
    async def create_user(name):
        async with session() as session:
            session.add(User(name=name))
            await session.commit()
