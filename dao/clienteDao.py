#!/usr/bin/env python3
import sqlalchemy.orm as orm
from model import entities

Session = orm.sessionmaker(bind=entities.engine)
session = Session()

class ClienteDao:
    def get_all_nomes(self):
        return session.query(entities.Cliente.nome).all()
        