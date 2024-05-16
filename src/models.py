import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    userid = Column(Integer,primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(50), unique=True)
    password = Column(String(32) nullable=True)

class People(Base):
    __tablename__ = 'people'

    peopleid = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=True)
    gender = Column(String(10), nullable=True)
    height = Column(Integer, nullable=True)
    mass = Column(Integer, nullable=True)

class Planet(Base):
    __tablename__ = 'planet'

    planetid = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=True)
    climate = Column(String(10), nullable=True)
    population = Column(Integer, nullable=True)
    gravity = Column(Integer, nullable=True)
    terrain = Column(Integer, nullable=True)

class Starships(Base):
    __tablename__ = 'starships'

    starshipsid = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=True)
    model = Column(String(10), nullable=True)
    cost = Column(Integer, nullable=True)
    pilot = Column(String(50), nullable=True)

class FavPlanet(Base):
    ___tablename__ = 'favplanet'

    id = Column(Integer, pimary_key=True)
    userid = Column(Integer, ForeignKey('user.userid'))
    userid_relationship = relationship(User)
    planetid = Column(Integer, ForeignKey('planet.planetid'))
    planetid_relationship = relationship(Planet)



class Address(Base):
   
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
