import sqlalchemy as db
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class mysqllib:
    def __init__(self, host, port, user, password, database):
        if not password:
            password = ""

        self.engine = db.create_engine("mysql+pymysql://{}:{}@{}:{}/{}"
                                       .format(user, password,
                                               host, port, database))

        self.meta = db.MetaData()
        print("Connected to mysql")

    """Insert log to to database"""
    def insertLog(self, log: Base):
        session = Session(self.engine)
        try:
            session.add(log)
            session.commit()
            return log
        except Exception as e:
            print(e)
            session.rollback()
        finally:
            session.close()

    def cleareTable(self, model: Base):
        session = Session(self.engine)
        try:
            num_rows_deleted = session.query(model).delete()
            session.commit()
            return num_rows_deleted
        except Exception as e:
            print(e)
            session.rollback()
        finally:
            session.close()
