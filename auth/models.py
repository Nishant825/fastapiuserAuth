from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, INTEGER, String, ForeignKey
from sqlalchemy.orm import relationship


Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(INTEGER, primary_key=True)
    first_name = Column(String(512), nullable=False)
    last_name = Column(String(512), nullable=False)
    username = Column(String(100),nullable=False, unique=True)
    email = Column(String(50),nullable=False)
    password = Column(String(20),nullable=False)
    token = relationship("Token",back_populates="user",uselist=False)

    def __str__(self):
        return self.username


class Token(Base):
    __tablename__ = "tokens"
    id = Column(INTEGER, primary_key=True)
    access_token = Column(String(50),nullable=False)
    user_id = Column(INTEGER,ForeignKey("users.id"))
    user = relationship("User",back_populates="token")

    def __str__(self):
        return self.user.username
