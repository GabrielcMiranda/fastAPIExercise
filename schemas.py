from pydantic import BaseModel
from typing import List

class UserCreateInput(BaseModel):
    name: str

class UserSongInput(BaseModel):
    user_id: int
    song_id: int


class UserSubOutput(BaseModel):
    id: int
    name: str
    
    class config:
        orm_mode = True
class SongGetOutput(BaseModel):
    id: int
    name: str
    duration: float
    composer: str
    liked_by: List[UserSubOutput]

    class config:
        orm_mode = True

class SongSubOutput(BaseModel):
    id: int
    name: str
    duration: float
    composer: str
    
    class config:
        orm_mode = True

class UserGetOutput(BaseModel):
    id: int
    name: str
    liked_songs: List[SongSubOutput]

    class Config:
        orm_mode= True
class SongCreateInput(BaseModel):
    name: str
    duration: float
    composer: str

class StandartOutput(BaseModel):
    message: str    

class ErrorOutput(StandartOutput):
    detail: str
