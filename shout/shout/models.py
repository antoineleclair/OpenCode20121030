from sqlalchemy import (
    Column,
    Integer,
    Unicode,
    DateTime,
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

from datetime import datetime

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()

class Broadcast(Base):
    __tablename__ = 'broadcasts'
    id = Column(Integer, primary_key=True)
    content = Column(Unicode)
    created = Column(DateTime, default=datetime.now)

    def __init__(self, content):
        self.content = content

