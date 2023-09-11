import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    favorites = relationship('Favorite', backref='user')
    

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=False)
    population = Column(String(250), nullable=False)
    diameter = Column(String(250), nullable=False)
    favorites = relationship('Favorite', backref='planet')


class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    hair_color=Column(String(250), nullable=True)
    gender=Column(String(250), nullable=True)
    birth_year=Column(String(250), nullable=False)
    favorites = relationship('Favorite', backref='person')


class Starship(Base):
    __tablename__ = 'starship'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250), nullable=False)
    passengers = Column(String(250), nullable=False)
    max_atmosphering_speed = Column(String(250), nullable=False)
    favorites = relationship('Favorite', backref='starship')


    
class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    favoriteStarshipId = Column(Integer, ForeignKey('starship.id'), nullable=True)
    favoritePersonId = Column(Integer, ForeignKey('person.id'), nullable=True)
    favoritePlanetId = Column(Integer, ForeignKey('planet.id'), nullable=True)
    user = relationship('User', backref='favorites')
    starship = relationship('Starship', backref='favorites')
    person = relationship('Person', backref='favorites')
    planet = relationship('Planet', backref='favorites')


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

# class FavoritePlanet(Base):
#     __tablename__ = 'favorite_planet'
#     id = Column(Integer, primary_key=True)
#     user_id = Column(Integer, ForeignKey('user.id'))
#     planet_id = Column(Integer, ForeignKey('planet.id'))
   
# class FavoritePerson(Base):
#     __tablename__ = 'favorite_person'
#     id = Column(Integer, primary_key=True)
#     user_id = Column(Integer, ForeignKey('user.id'))
#     person_id = Column(Integer, ForeignKey('person.id'))
   
# class FavoriteStarship(Base):
#     __tablename__ = 'favorite_starship'
#     id = Column(Integer, primary_key=True)
#     user_id = Column(Integer, ForeignKey('user.id'))
#     starship_id = Column(Integer, ForeignKey('starship.id'))