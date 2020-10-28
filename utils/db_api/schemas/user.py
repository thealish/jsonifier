from utils.db_api.db_gino import TimeBaseModel
from sqlalchemy import Integer, Column, BigInteger, String, sql


class User(TimeBaseModel):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    email = Column(String(100))

    referral = Column(BigInteger)

    query: sql.Select