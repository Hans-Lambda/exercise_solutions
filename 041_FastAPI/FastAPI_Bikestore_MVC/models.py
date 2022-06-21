from pydantic import BaseModel
from datetime import datetime
from typing import Callable
import uuid


class Partner(BaseModel):

    name: str
    email: str
    username: str
    password: str
    bike: list


class Client(BaseModel):

    name: str
    email: str
    username: str
    password: str


class Bike(BaseModel):

    id_: str
    name: str
    manufacturer: str
    year: str
    #partner: Partner


class Bill(BaseModel):

    bike: list
    client: Client
    partner: Partner
    date: datetime
    id: str
    billing_method: str
    status: str
    billing: Callable[[int], int]
