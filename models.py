from sqlalchemy import Column, Integer, Double, String, ForeignKey, Table
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

user_music = Table(
        'user_music',
        Base.metadata,
        Column('user_id',Integer, ForeignKey('user.id'),primary_key=True),
        Column('music_id',Integer,ForeignKey('music.id'),primary_key=True)
    )
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key = True, autoincrement=True)
    name = Column(String)
    favoriteMusics = relationship('Music', secondary=user_music, back_populates="listeners")
class Music(Base):
    __tablename__ = 'music'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    duration = Column(Double)
    composer = Column(String)
    listeners = relationship('User', secondary=user_music, back_populates='favoriteMusics')

   
