from datetime import datetime
from typing import Optional, List
from sqlmodel import SQLModel, Field, Column
from sqlalchemy import JSON

"""
class User(SQLModel, table=True):
    __tablename__ = "user":
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    email: str
    password: str
    active: bool
    created_at: datetime
    updated_at: datetime

"""

    

