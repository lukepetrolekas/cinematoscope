from sqlalchemy import *
import datetime

metadata_obj = MetaData()

# When all are primary key, it is used to ensure deduplication.

# SQLAlchemy docs:

# It is also recommended, though not in any way required by SQLAlchemy, that the 
# columns which refer to the two entity tables are established within either a 
# unique constraint or more commonly as the primary key constraint; this ensures
# that duplicate rows won’t be persisted within the table regardless of issues 
# on the application side:

# Concepts ---------------------------------------------------------------------

language = Table('language', metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('name', String(64), nullable=False, default="", unique=True),
    Column('iso639', String(10), nullable=False, default="", unique=True),
    Column('prevalence', Integer, nullable=False, default=1, unique=True)
    )

genre = Table('genre', metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('name', String(64), nullable=False, default="", unique=True),
    Column('wiki_qid', BigInteger, nullable=False, default=0, unique=True))

# A medium on which a film may be portrayed (DVD, Blu-Ray, Netflix)
medium = Table('medium', metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('name', String(64), nullable=False, default="", unique=True),
    Column('is_stream', Boolean, nullable=False, default=False))

# A Film -----------------------------------------------------------------------

film = Table('film', metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('title', String(128), nullable=False, default=""),
    Column('publication_date', Date, nullable=False, default=datetime.datetime.now()),
    Column('sound', SmallInteger, nullable=False, default=1),
    Column('color', SmallInteger, nullable=False, default=1),
    Column('duration', Integer, nullable=False, default=0),  # In seconds
    Column('wiki_qid', BigInteger, nullable=False, default=0, unique=True))

film_language = Table('film_language', metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('film_id', ForeignKey('film.id'), primary_key=True),
    Column('language_id', ForeignKey('language.id'), primary_key=True))

film_genre = Table('film_genre', metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('film_id', ForeignKey('film.id'), nullable=False, primary_key=True),
    Column('genre_id', ForeignKey('genre.id'), nullable=False, primary_key=True))

# A promotional poster for the film
poster = Table('poster', metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('film_id', ForeignKey('film.id'), nullable=False, primary_key=True),
    Column('poster_hash', String(64), nullable=False, default="", primary_key=True))

# Any character portrayed in film
character = Table('character', metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('name', String(64), nullable=False, default="", unique=True),
    Column('wiki_qid', BigInteger, nullable=False, default=0, unique=True))

# Employment ---------------------------------------------------------------

# A person, a collective, corporation, or other entity
entity = Table('entity', metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('name', String(255), nullable=False, default=""),
    Column('wiki_qid', BigInteger, default=0, unique=True))

# jobs in making a film
job = Table('job', metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('name', String(128), nullable=False, default="", unique=True),
    Column('wiki_qid', BigInteger, default=0, unique=True))

# how an entity has participated in making a film
film_job = Table('film_job', metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('entity_id', ForeignKey('entity.id'), primary_key=True),
    Column('job_id', ForeignKey('job.id'), primary_key=True),
    Column('film_id', ForeignKey('film.id'), primary_key=True))

# an actor portraying a character
role = Table('role', metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('film_id', ForeignKey('film.id'), nullable=False),
    Column('character_id', ForeignKey('character.id'), nullable=False),
    Column('entity_id', ForeignKey('entity.id'), nullable=False))

# User's Items -----------------------------------------------------------------

# The physical or digital object owned or streamed by the user
film_object = Table('film_object', metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('film_id', ForeignKey('film.id'), nullable=False),
    Column('medium_id', ForeignKey('medium.id'), nullable=False),
    Column('created', DateTime, nullable=False, default=datetime.datetime.now),
    Column('updated', DateTime, onupdate=datetime.datetime.now)) 

# User's Organization ----------------------------------------------------------

# The user's categories
category = Table('category', metadata_obj,
    Column('id', primary_key=True),
    Column('category', String(64), nullable=False, unique=True),
    Column('color', Integer, nullable=False, default=0))

film_category = Table('identifier', metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('film_object_id', ForeignKey('film_object.id'), nullable=False, primary_key=True),
    Column('category_id', ForeignKey('category.id'), nullable=False, primary_key=True))

# User's Data ------------------------------------------------------------------

# Some users like leaving notes, maintain similar functionality
note = Table('note', metadata_obj,
    Column('id', primary_key=True),
    Column('film_object_id', ForeignKey('film_object.id'), nullable=False),
    Column('note', Text()))

# User and friends/members of household
user = Table('user', metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('name', String(64), nullable=False, default="", unique=True))

# Log who has watched what film
watched = Table('watched', metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('user_id', ForeignKey('user.id'), nullable=False, primary_key=True),
    Column('film_id', ForeignKey('film.id'), nullable=False, primary_key=True))

# Log for films yet to acquire/stream
wishlist = Table('wishlist', metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('user_id', ForeignKey('user.id'), nullable=False, primary_key=True),
    Column('film_id', ForeignKey('film.id'), nullable=False, primary_key=True))

# favourites
favorites = Table('favorites', metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('user_id', ForeignKey('user.id'), nullable=False, primary_key=True),
    Column('film_id', ForeignKey('film.id'), nullable=False, primary_key=True))

# personal rating
rating = Table('rating', metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('user_id', ForeignKey('user.id'), nullable=False, primary_key=True),
    Column('film_id', ForeignKey('film.id'), nullable=False, primary_key=True),
    Column('rating', SmallInteger, default=0, primary_key=True))