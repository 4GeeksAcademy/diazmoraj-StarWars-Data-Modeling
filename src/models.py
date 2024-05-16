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
    password = Column(String(32), nullable=True)

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
    pilot = Column(Integer, nullable=True)

class FavPlanet(Base):
    __tablename__ = 'favplanet'

    favplanetid = Column(Integer, primary_key=True)
    userid = Column(Integer, ForeignKey('user.userid'))
    userid_relationship = relationship(User)
    planetid = Column(Integer, ForeignKey('planet.planetid'))
    planetid_relationship = relationship(Planet)

class FavPeople(Base):
    __tablename__ = 'favpeople'
    favpleopleid = Column(Integer, primary_key=True)
    userid = Column(Integer, ForeignKey('user.userid'))
    userid_relationship = relationship(User)
    peopleid = Column(Integer, ForeignKey('peoplet.peopleid'))
    peopleid_relationship = relationship(People)

class FavStarships(Base):
    __tablename__ = 'favstarships'
    favstartshipsid = Column(Integer, pr  imary_key=True)
    userid = Column(Integer, ForeignKey('user.userid'))
    userid_relationship = relationship(User)
    starshipsid = Column(Integer, ForeignKey('starships.starshipsid'))
    starshipsid_relationship = relationship(Starships)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
