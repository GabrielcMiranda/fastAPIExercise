from pydantic import BaseModel

class UserCreateInput(BaseModel):
    name: str

class UserIdInput(BaseModel):
    id: int

class StandartOutput(BaseModel):
    message: str    

class ErrorOutput(StandartOutput):
    detail: str