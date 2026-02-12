"""UserRepository — async SQLAlchemy."""
from __future__ import annotations

from app.security import hash_password, verify_password

from sqlalchemy import select, func
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.db import UserORM
from app.models.user import UserCreate


class UserRepository:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def create(self, data: UserCreate) -> UserORM:
        user = UserORM(
            username=data.username,
            email=data.email,
            hashed_password=hash_password(data.password),
        )
        self._session.add(user)
        try:
            # nested savepoint — позволяет поймать IntegrityError
            # без порчи внешней транзакции (важно для тестов с rollback)
            async with self._session.begin_nested():
                await self._session.flush()
            await self._session.refresh(user)
        except IntegrityError:
            raise
        return user

    async def get_by_id(self, user_id: int) -> UserORM | None:
        result = await self._session.execute(
            select(UserORM).where(UserORM.id == user_id)
        )
        return result.scalar_one_or_none()

    async def get_by_email(self, email: str) -> UserORM | None:
        result = await self._session.execute(
            select(UserORM).where(UserORM.email == email.lower())
        )
        return result.scalar_one_or_none()

    async def list(self, limit: int = 20, offset: int = 0) -> list[UserORM]:
        result = await self._session.execute(
            select(UserORM).order_by(UserORM.id).limit(limit).offset(offset)
        )
        return list(result.scalars().all())

    async def count(self) -> int:
        result = await self._session.execute(select(func.count(UserORM.id)))
        return result.scalar_one()

    async def delete(self, user_id: int) -> bool:
        user = await self.get_by_id(user_id)
        if not user:
            return False
        await self._session.delete(user)
        await self._session.flush()
        return True
