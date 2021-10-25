from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
from config import CONNECTION_STRING, DB_NAME


Base = declarative_base()


class DBObject(object):
    def to_dict(self):
        result = {}
        insp = inspect(self)
        for c in insp.mapper.attrs.keys():
            atribute = getattr(self, c)
            if isinstance(atribute, list):
                result[c] = [self._item_to_dict(a) for a in atribute]
            else:
                result[c] = self._item_to_dict(atribute)

        return result

    def _item_to_dict(self, item):
        if isinstance(item, Base):
            return item.to_dict()
        return item


def postgresql_engine(pool_size=1, max_overflow=25):
    dbname = DB_NAME
    con_str = CONNECTION_STRING
    engine = create_engine(
        "postgresql+psycopg2://{}/{}".format(con_str, dbname),
        pool_size=pool_size,
        max_overflow=max_overflow,
        pool_recycle=30 * 60,
    )
    return engine


engine = postgresql_engine()


class DBContext(object):
    def __init__(self, engine):
        self.session = None
        self.engine = engine

    def __enter__(self):
        session = sessionmaker()
        self.session = session(bind=self.engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.rollback()
        self.session.close()


def setup_database():
    psql_url = f"postgresql+psycopg2://{CONNECTION_STRING}"
    psql_engine = create_engine(psql_url)

    def drop_database():
        engine.dispose()
        conn = psql_engine.connect()
        conn.execute("commit")
        conn.execute(f"drop database {DB_NAME}")

    def create_database():
        conn = psql_engine.connect()
        conn.execute("commit")
        try:
            conn.execute(f"create database {DB_NAME}")
        except Exception:
            pass
        conn.close()
        conn = engine.connect()
        conn.execute("commit")

        try:
            conn.execute("create schema boitatech")
        except Exception:
            pass
        conn.execute("commit")

    create_database()
