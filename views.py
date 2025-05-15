from fastapi import APIRouter, HTTPException
from services import UserService
from schemas import UserCreateInput, StandartOutput, ErrorOutput, UserIdInput

user_router = APIRouter(prefix='/user')
assets_router = APIRouter(prefix='/assets')

@user_router.post('/create',description='crie um registro de usuario', response_model= StandartOutput, responses={400:{'model': ErrorOutput}})
async def create_user(user_input: UserCreateInput):
    try:
        await UserService.create_user(name=user_input.name)
        return StandartOutput(message='ok')
    except Exception as error:
        raise HTTPException(400,detail=str(error))

@user_router.delete('/delete',description='delete um usuario pelo id', response_model = StandartOutput, responses={400:{'model':ErrorOutput}})
async def delete_user(input_id: int):
    try:
        await UserService.delete_user(id=input_id)
        return StandartOutput(message='ok')
    except Exception as error:
        raise HTTPException(400,detail=str(error))