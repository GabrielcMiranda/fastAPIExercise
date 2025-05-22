from fastapi import APIRouter, HTTPException
from services import UserService, SongService
from schemas import UserCreateInput, StandartOutput, ErrorOutput, SongCreateInput, UserGetOutput, UserSongInput, SongGetOutput
from typing import List

user_router = APIRouter(prefix='/user')
song_router = APIRouter(prefix='/song')

@user_router.post('/create',tags=['User'],description='crie um registro de usuario', response_model= StandartOutput, responses={400:{'model': ErrorOutput}})
async def create_user(user_input: UserCreateInput):
    try:
        await UserService.create_user(name=user_input.name)
        return StandartOutput(message='usuario criado com sucesso')
    except Exception as error:
        raise HTTPException(400,detail=str(error))

@user_router.delete('/delete',tags=['User'],description='delete um usuario pelo id',response_model = StandartOutput, responses={400:{'model':ErrorOutput}})
async def delete_user(input_id: int):
    try:
        await UserService.delete_user(id=input_id)
        return StandartOutput(message='usuario deletado com sucesso')
    except Exception as error:
        raise HTTPException(400,detail=str(error))
    
@user_router.get('/get',tags=['User'],description='retorna um usuario a partir do id',response_model= UserGetOutput,responses={400:{'model':ErrorOutput}})
async def get_user(input_id: int):
    try: 
        return await UserService.get_user(id=input_id)
    except Exception as error:
        raise HTTPException(400,detail= str(error))
    
@user_router.post('/like',tags=['User'],description='associa uma musica a um usuario por meio de uma curtida',response_model=StandartOutput,responses={400:{'model':ErrorOutput}})
async def like_song(input: UserSongInput):
    try:
        await UserService.like_song(user_id=input.user_id, song_id=input.song_id)
        return StandartOutput(message='musica curtida com sucesso')
    except Exception as error:
        raise HTTPException(400,detail=str(error))
    
@song_router.post('/create',tags=['Song'],description='crie um registro de musica', response_model=StandartOutput, responses={400:{'model': ErrorOutput}})
async def create_song(user_input: SongCreateInput):
    try:
        await SongService.create_song(name = user_input.name, duration = user_input.duration, composer = user_input.composer)
        return StandartOutput(message='musica criada com sucesso')
    except Exception as error:
        raise HTTPException(400, detail=str(error))
    
@song_router.delete('/delete',tags=['Song'],description='delete uma musica pelo id',response_model=StandartOutput, responses={400:{'model':ErrorOutput}})
async def delete_song(input_id: int):
    try:
        await SongService.delete_song(id=input_id)
        return StandartOutput(message='musica deletada com sucesso')
    except Exception as error:
        raise HTTPException(400, detail=str(error))
    
@song_router.get('/get',tags=["Song"],description='retorna uma musica a partir do id', response_model= SongGetOutput, responses={400:{'model': ErrorOutput}})
async def get_song(input_id : int):
    try:
        return await SongService.get_song(id= input_id)
    except Exception as error:
        raise HTTPException(400,detail= str(error))
    