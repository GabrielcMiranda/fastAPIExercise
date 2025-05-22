from fastapi import APIRouter, HTTPException
from services import SongService
from schemas import StandartOutput, ErrorOutput, SongCreateInput, SongGetOutput, SongSubOutput
from typing import List

song_router = APIRouter(prefix='/song')
    
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

@song_router.get('/list',tags=['Song'], description='retorna uma lista com todas as musicas do banco', response_model=List[SongSubOutput],responses={400:{'model': ErrorOutput}})
async def list_songs():
    try:
        return await SongService.list_songs()
    except Exception as error:
        raise HTTPException(400,detail= str(error))
    