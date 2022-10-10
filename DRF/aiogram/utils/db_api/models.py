from sqlalchemy import (Column, Integer, String, ForeignKey, BigInteger)
from sqlalchemy import sql
from utils.db_api.database import db


class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    user_id = Column(BigInteger)
    full_name = Column(String(100))
    username = Column(String(50))
    phone_number = Column(String(50), nullable=True)
    query: sql.Select

    def __repr__(self):
        return "<User(id='{}', fullname='{}', username='{}')>".format(
            self.id, self.full_name, self.username)


class Rating(db.Model):
    __tablename__ = 'ratings'

    id = Column(Integer, primary_key=True)
    ratinger = Column(Integer) #raiting qoyayotgan user_id
    whos_reting = Column(Integer) # raiting olayotgan
    rating = Column(Integer)
    query: sql.Select


    def __repr__(self):
        return "<Rating(ratinger='{}', whos_reting='{}', rating='{}')>".format(
            self.ratinger, self.whos_reting, self.rating)
