import os
import asyncio
import aiohttp
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, selectinload, joinedload, relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from typing import List, Dict, Tuple

DATABASE_URL = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://potus:potus@localhost/HW4"

engine = create_async_engine(DATABASE_URL, echo=True)
async_session = sessionmaker(bind=engine, expire_on_commit=False, class_=AsyncSession)
Base = declarative_base()

# Модели
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)

    posts = relationship("Post", back_populates="user")

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    title = Column(String, nullable=False)
    body = Column(String, nullable=False)

    user = relationship("User", back_populates="posts")

# Функция для создания таблиц
async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# Функция для очистки таблиц
async def clear_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

# Функция для загрузки данных по URL
async def fetch_url(session, url):
    async with session.get(url) as response:
        return await response.json()

# Функции для загрузки данных пользователей и постов
async def fetch_users_data():
    url = 'https://jsonplaceholder.typicode.com/users'
    async with aiohttp.ClientSession() as session:
        return await fetch_url(session, url)

async def fetch_posts_data():
    url = 'https://jsonplaceholder.typicode.com/posts'
    async with aiohttp.ClientSession() as session:
        return await fetch_url(session, url)

# Функции для добавления данных в базу данных
async def add_users(session: AsyncSession, users_data):
    users = [User(name=user['name'], username=user['username'], email=user['email']) for user in users_data]
    session.add_all(users)
    await session.commit()

async def add_posts(session: AsyncSession, posts_data):
    try:
        posts = [Post(user_id=post['userId'], title=post['title'], body=post['body']) for post in posts_data]
        session.add_all(posts)
        await session.commit()
    except Exception as e:
        print(f"Error adding posts: {e}")
        await session.rollback()

# Основная асинхронная функция
async def async_main():
    await clear_tables()

    users_data, posts_data = await asyncio.gather(
        fetch_users_data(),
        fetch_posts_data()
    )

    async with async_session() as session:
        await add_users(session, users_data)
        await add_posts(session, posts_data)

    await engine.dispose()

# Запуск основной функции
def main():
    asyncio.run(async_main())

if __name__ == "__main__":
    main()