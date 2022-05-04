import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    password = Column(String(15), nullable=False)
    first_name = Column(String(15), nullable=False)
    last_name = Column(String(15), nullable=False)
    email = Column(String(50), nullable=False, unique = True)
    post = relationship("Post", backref = "user")
    following = relationship('Following', backref = "user", uselist = True)
    follower = relationship('Follower', backref = "user", uselist = True)
    

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    caption = Column(String(250))
    image = Column(String(250)) #URL#
    saved = relationship('Saved', backref = "post", uselist = True)
    liked = relationship('Liked', backref = "post", uselist = True)
    comment = relationship('Comment', backref = "post", uselist = True)
   

class Following(Base):
    __tablename__ = 'following'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    


class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    


class Saved(Base):
    __tablename__ = 'saved'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('post.id'))


class Liked(Base):
    __tablename__ = 'liked'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('post.id'))

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('post.id'))
    
    
    
## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
