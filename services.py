from models import User, Song
from connection import session
from sqlalchemy import delete

class UserService:
    async def create_user(name):
        async with session() as sessao:
            sessao.add(User(name=name))
            await sessao.commit()

    async def delete_user(id):
        async with session() as sessao:
            await sessao.execute(delete(User).where(User.id == id))
            await sessao.commit()

class SongService:
    async def create_song(name,duration,composer):
        async with session() as sessao:
            sessao.add(Song(name=name, duration=duration, composer=composer))
            await sessao.commit()

    async def delete_song(id):
        async with session() as sessao:
            await sessao.execute(delete(Song).where(Song.id == id))
            await sessao.commit()