from models import User, Song
from connection import session
from sqlalchemy import delete
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload

class UserService:
    async def create_user(name):
        async with session() as sessao:
            sessao.add(User(name=name))
            await sessao.commit()

    async def delete_user(id):
        async with session() as sessao:
            await sessao.execute(delete(User).where(User.id == id))
            await sessao.commit()
    
    async def get_user(id):
        async with session() as sessao:
            result = await sessao.execute(select(User).options(selectinload(User.liked_songs)).where(User.id == id))
            return result.scalar_one_or_none()
    
    async def like_song(user_id, song_id):
        async with session() as sessao:
            user_result = await sessao.execute(select(User).where(User.id == user_id))
            user = user_result.scalar_one_or_none()

            song_result = await sessao.execute(select(Song).where(Song.id == song_id))
            song = song_result.scalar_one_or_none()

            if not user or not song:
                raise Exception("Usuário ou música não encontrada")
            
            if song not in user.liked_songs:
                user.liked_songs.append(song)
                await sessao.commit()

    async def update_username(user_id: int, new_name: str):
        async with session() as sessao:
            result = await sessao.execute(select(User).where(User.id == user_id))
            user = result.scalar_one_or_none()

            if not user:
                raise Exception("usuario nao encontrado")
            
            user.name = new_name
            await sessao.commit()

    async def list_users():
        async with session() as sessao:
            result = await sessao.execute(select(User))
            return result.scalars().all()


class SongService:
    async def create_song(name,duration,composer):
        async with session() as sessao:
            sessao.add(Song(name=name, duration=duration, composer=composer))
            await sessao.commit()

    async def delete_song(id):
        async with session() as sessao:
            await sessao.execute(delete(Song).where(Song.id == id))
            await sessao.commit()

    async def get_song(id):
        async with session() as sessao:
            result = await sessao.execute(select(Song).options(selectinload(Song.liked_by)).where(Song.id == id))
            return result.scalar_one_or_none()
        
    async def list_songs():
        async with session() as sessao:
            result = await sessao.execute(select(Song))
            return result.scalars().all()