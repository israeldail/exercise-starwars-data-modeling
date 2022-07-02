import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()
class UserLogin(Base):
    __tablename__ = 'user_login'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    firstName = Column(String(250))
    lastName = Column(String(250))
    user_name = Column(String(250), nullable=False)
    email_address = Column(String(250), nullable=False)
    userlogin_id = Column(Integer, ForeignKey(UserLogin.id))
    userlogin = relationship(UserLogin)

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

class Characters(Base):
    __tablename__ = "characters"
    id = Column(Integer, primary_key=True)
    character_name = Column(String(250))
    homeworld = Column(String(250))
    gender = Column(String(250))
    height = Column(String(250))
    mass = Column(Integer, ForeignKey('mass'))
    eye_color = Column(String(250))


class Planets(Base):
    __tablename__ = "planets"
    id = Column(Integer, primary_key=True)
    planet_name = Column(String(250))
    planet_mass = Column(Integer, ForeignKey('planet_mass'))
    planet_coordinates = Column(Integer, ForeignKey('planet_coordinates'))

class FavoritePlanet(Base):
    __tablename__ = "favorite_planets"
    id = Column(Integer, primary_key=True)
    user_favorite_planet = Column(String(250), ForeignKey('planets.id'))
    planet_id = relationship(Planets)
    user_profile = Column(Integer, ForeignKey('user.id'))
    user_id = relationship(User)

class FavoriteChar(Base):
    __tablename__ = "favorite_characters"
    id = Column(Integer, primary_key=True)
    user_favorite_char = Column(String(250), ForeignKey('characters.id'))
    characters_id = relationship(Characters)
    user_profile = Column(Integer, ForeignKey('user.id'))
    user_id = relationship(User)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')