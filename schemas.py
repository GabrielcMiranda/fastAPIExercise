from pydantic import BaseModel

class UserCreateInput(BaseModel):
    name: str
class SongCreateInput(BaseModel):
    name: str
    duration: float
    composer: str

class StandartOutput(BaseModel):
    message: str    

class ErrorOutput(StandartOutput):
    detail: str