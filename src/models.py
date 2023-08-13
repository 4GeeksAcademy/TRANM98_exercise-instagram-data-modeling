import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(Integer, unique=True, nullable=False )
    email = Column(String(250),unique=True, nullable=False)
    password_hash = Column(String(250), nullable=False)
    profile_img = Column(String)
    bio =Column(String(250))
    followers = relationship("Follow", foreign_keys='Follow.followed_id', back_populates="followed_by")
    following = relationship("Follow", foreign_keys='Follow.follower_id', back_populates="follower_of")
    posts = relationship("Post", back_populates="user")

class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    image_url = Column(String, nullable=False)
    caption = Column(String)
    likes = relationship("Like", back_populates="post")
    comments = relationship("Comment", back_populates="post")
class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    text = Column(String(250), nullable=False)

class Like(Base):
    __tablename__ = 'like'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))

class Follow(Base):
    __tablename__ = 'follow'
    id = Column(Integer, primary_key=True)
    follower_id = Column(Integer, ForeignKey('user.id'))
    followed_id = Column(Integer, ForeignKey('user.id'))
    follower_of = relationship("User", foreign_keys=[follower_id], back_populates="followers")
    followed_by = relationship("User", foreign_keys=[followed_id], back_populates="following")


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
