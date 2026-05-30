"""Users API router."""

from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies import get_current_user, get_db
from app.models.user import UserCreate, UserListResponse, UserResponse
from app.repositories.user_repo import UserRepository

router = APIRouter(prefix="/api/v1/users", tags=["users"])


@router.post("", response_model=UserResponse, status_code=201)
async def create_user(
    data: UserCreate,
    db: AsyncSession = Depends(get_db),
) -> UserResponse:
    repo = UserRepository(db)
    try:
        user = await repo.create(data)
        await db.commit()
        return UserResponse.model_validate(user)
    except IntegrityError:
        raise HTTPException(status_code=409, detail="Email already registered") from None


@router.get("", response_model=UserListResponse)
async def list_users(
    limit: int = Query(default=20, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
    db: AsyncSession = Depends(get_db),
    _: dict = Depends(get_current_user),
) -> UserListResponse:
    repo = UserRepository(db)
    items = await repo.list(limit=limit, offset=offset)
    total = await repo.count()
    return UserListResponse(
        items=[UserResponse.model_validate(u) for u in items],
        total=total,
        limit=limit,
        offset=offset,
    )


@router.get("/{user_id}", response_model=UserResponse)
async def get_user(
    user_id: int,
    db: AsyncSession = Depends(get_db),
    _: dict = Depends(get_current_user),
) -> UserResponse:
    repo = UserRepository(db)
    user = await repo.get_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return UserResponse.model_validate(user)


@router.delete("/{user_id}", status_code=204)
async def delete_user(
    user_id: int,
    db: AsyncSession = Depends(get_db),
    _: dict = Depends(get_current_user),
) -> None:
    repo = UserRepository(db)
    deleted = await repo.delete(user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")
    await db.commit()
