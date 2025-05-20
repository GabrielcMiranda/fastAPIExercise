from fastapi import APIRouter, HTTPException
from services import UserService, SongService
from schemas import UserCreateInput, StandartOutput, ErrorOutput, SongCreateInput

user_router = APIRouter(prefix='/user')
song_router = APIRouter(prefix='/song')

@user_router.post('/create',tags=['User'],description='crie um registro de usuario', response_model= StandartOutput, responses={400:{'model': ErrorOutput}})
async def create_user(user_input: UserCreateInput):
    try:
        await UserService.create_user(name=user_input.name)
        return StandartOutput(message='ok')
    except Exception as error:
        raise HTTPException(400,detail=str(error))

@user_router.delete('/delete',tags=['User'],description='delete um usuario pelo id',response_model = StandartOutput, responses={400:{'model':ErrorOutput}})
async def delete_user(input_id: int):
    try:
        await UserService.delete_user(id=input_id)
        return StandartOutput(message='ok')
    except Exception as error:
        raise HTTPException(400,detail=str(error))
    
@song_router.post('/create',tags=['Song'],description='crie um registro de musica', response_model=StandartOutput, responses={400:{'model': ErrorOutput}})
async def create_song(user_input: SongCreateInput):
    try:
        await SongService.create_song(name = user_input.name, duration = user_input.duration, composer = user_input.composer)
        return StandartOutput(message='ok')
    except Exception as error:
        raise HTTPException(400, detail=str(error))
    
@song_router.delete('/delete',tags=['Song'],description='delete uma musica pelo id',response_model=StandartOutput, responses={400:{'model':ErrorOutput}})
async def delete_song(input_id: int):
    try:
        await SongService.delete_song(id=input_id)
        return StandartOutput(message='musica deletada com sucesso')
    except Exception as error:
        raise HTTPException(400, detail=str(error))