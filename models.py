from sqlalchemy import Column, Integer, Double, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key = True, autoincrement=True)
    name = Column(String)
    favoriteMusics = relationship('Music', backref='user')

#do jeito que ta, a relacao fica de um pra muitos, ou seja, uma instancia de musica nao pode ser salva por mais de um usuario
class Music(Base):
    __tablename__ = 'music'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    duration = Column(Double)
    composer = Column(String)
    user_id = Column(Integer, ForeignKey('user.id'))
