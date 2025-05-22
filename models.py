from sqlalchemy import Column, Integer, Double, String, ForeignKey, Table
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

user_song = Table(
        'user_song',
        Base.metadata,
        Column('user_id',Integer, ForeignKey('user.id'),primary_key=True),
        Column('song_id',Integer,ForeignKey('song.id'),primary_key=True)
    )
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key = True, autoincrement=True)
    name = Column(String)
    liked_songs = relationship('Song', secondary=user_song, back_populates="liked_by", lazy='subquery')
class Song(Base):
    __tablename__ = 'song'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    duration = Column(Double)
    composer = Column(String)
    liked_by = relationship('User', secondary=user_song, back_populates='liked_songs', lazy='subquery')

   
