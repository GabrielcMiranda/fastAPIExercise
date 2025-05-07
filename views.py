from fastapi import APIRouter
from services import UserService
from schemas import UserCreateInput, StandartOutput

user_router = APIRouter(prefix='/user')
assets_router = APIRouter(prefix='/assets')

@user_router.post('/create', response_model= StandartOutput)
async def create_user(user_input: UserCreateInput):
    try:
        await UserService.create_user(name=user_input.name)
        return StandartOutput(message='ok')
    except:
        pass