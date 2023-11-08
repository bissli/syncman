import sqlalchemy as sa
from sqlalchemy.orm import declarative_base
from syncman import config

Base = declarative_base()


class Node(Base):
    __tablename__ = f'{config.sql.appname}node'

    Name = sa.Column('name', sa.String(255), primary_key=True)
    Created = sa.Column('created', sa.TIMESTAMP(timezone=False), primary_key=True)

    def __repr__(self):
        return "<Node(Name='%s', Created='%s')>" % (self.Name, self.Created)


class Sync(Base):
    __tablename__ = f'{config.sql.appname}sync'

    Id = sa.Column('id', sa.INTEGER, primary_key=True, autoincrement=True)
    Node = sa.Column('node', sa.String(255), nullable=False)
    Item = sa.Column('item', sa.String(255), nullable=False)

    def __repr__(self):
        return "<Sync(Node='%s', Item='%s')>" % (self.Node, self.Item)


class Audit(Base):
    __tablename__ = f'{config.sql.appname}audit'

    Id = sa.Column('id', sa.INTEGER, primary_key=True, autoincrement=True)
    Created = sa.Column('created', sa.TIMESTAMP(timezone=False), nullable=False)
    Node = sa.Column('node', sa.String(255), nullable=False)
    Item = sa.Column('item', sa.String(255), nullable=False)
    Date = sa.Column('date', sa.DATE(), nullable=False)

    def __repr__(self):
        return "<Audit(Node='%s', Created='%s', Item='%s')>" % (self.Node, self.Created, self.Item)


def create_tables(cn, drop=False):
    engine = cn.bind
    if drop:
        Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine, checkfirst=True)
