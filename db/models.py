from typing import List
from sqlalchemy import ForeignKey, String, DateTime, Float
from sqlalchemy.orm import  Mapped, mapped_column, relationship
from .config import Base

class Users(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(30))
    password: Mapped[str]

    categories: Mapped[List["Categories"]] = relationship(back_populates="user", cascade="all, delete-orphan")
    expenses: Mapped[List["Expenses"]] = relationship(back_populates="user", cascade="all, delete-orphan")
    
    def __repr__(self) -> str:
        return f"User(id={self.id!r}, username={self.username!r})"

class Categories(Base):
    __tablename__ = "categories"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    user: Mapped["Users"] = relationship(back_populates="categories")
    expenses: Mapped[List["Expenses"]] = relationship(back_populates="category", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"
    
class Expenses(Base):
    __tablename__ = "expenses"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    description: Mapped[str] = mapped_column(String(300), nullable=True)
    amount: Mapped[float] = mapped_column(Float)
    date: Mapped[str] = mapped_column(DateTime)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))

    user: Mapped["Users"] = relationship(back_populates="expenses")
    category: Mapped["Categories"] = relationship(back_populates="expenses")

    def __repr__(self) -> str:
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"