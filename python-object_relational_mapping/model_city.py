#!/usr/bin/python3
"""model de city"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.sql import True_
from model_state import Base, State


class City(Base):
    """class city"""
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement='auto')

    name = Column(String(128), nullable=False)
    stete_id = Column(Integer, ForeignKey('states.id'),
                      nullable=False)

    def __init__(self, name, state_id):
        """metodo de inicio"""
        self.name = name
        self.stete_id = state_id
