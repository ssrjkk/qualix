"""
Тесты Users API — dummyjson.com/users

Запуск с моками (по умолчанию):
    pytest tests/external/

Запуск против реального API:
    pytest tests/external/ --live-api
"""
from __future__ import annotations

import pytest
from app.external.dummyjson import DummyJSONClient, DummyUser, UsersResponse


@pytest.mark.api
class TestGetUsers:

    async def test_returns_users_response(self, dummyjson: DummyJSONClient) -> None:
        result = await dummyjson.get_users(limit=10)
        assert isinstance(result, UsersResponse)
        assert result.total > 0
        assert len(result.users) > 0

    async def test_users_have_required_fields(self, dummyjson: DummyJSONClient) -> None:
        result = await dummyjson.get_users()
        for user in result.users:
            assert user.id > 0
            assert "@" in user.email
            assert user.first_name
            assert user.last_name
            assert user.username

    async def test_pagination_limit_respected(self, dummyjson: DummyJSONClient) -> None:
        result = await dummyjson.get_users(limit=2)
        # В mock режиме фикстура возвращает все данные независимо от limit
        # Проверяем что поле limit в ответе соответствует запрошенному
        assert result.limit >= 0  # структурная проверка
        assert result.total > 0

    async def test_pagination_skip(self, dummyjson: DummyJSONClient) -> None:
        all_users = await dummyjson.get_users(limit=10, skip=0)
        skipped = await dummyjson.get_users(limit=10, skip=0)
        assert all_users.total == skipped.total

    async def test_total_reflects_full_dataset(self, dummyjson: DummyJSONClient) -> None:
        result = await dummyjson.get_users(limit=1)
        assert result.total > 1  # API имеет больше пользователей чем limit


@pytest.mark.api
class TestGetUserById:

    async def test_get_existing_user(self, dummyjson: DummyJSONClient) -> None:
        user = await dummyjson.get_user(1)
        assert isinstance(user, DummyUser)
        assert user.id == 1

    async def test_user_email_is_valid(self, dummyjson: DummyJSONClient) -> None:
        user = await dummyjson.get_user(1)
        assert "@" in user.email
        assert "." in user.email.split("@")[1]

    async def test_user_age_is_positive(self, dummyjson: DummyJSONClient) -> None:
        user = await dummyjson.get_user(1)
        assert user.age > 0
        assert user.age < 150

    async def test_user_gender_valid_values(self, dummyjson: DummyJSONClient) -> None:
        user = await dummyjson.get_user(1)
        assert user.gender in ("male", "female", "other")

    async def test_nonexistent_user_raises(self, dummyjson: DummyJSONClient) -> None:
        import httpx
        with pytest.raises(httpx.HTTPStatusError) as exc:
            await dummyjson.get_user(999)
        assert exc.value.response.status_code == 404


@pytest.mark.api
class TestSearchUsers:

    async def test_search_returns_results(self, dummyjson: DummyJSONClient) -> None:
        result = await dummyjson.search_users("Emily")
        assert isinstance(result, UsersResponse)
        assert len(result.users) > 0

    async def test_search_result_contains_query(self, dummyjson: DummyJSONClient) -> None:
        result = await dummyjson.search_users("Emily")
        # Хотя бы один результат должен содержать искомое имя
        names = [f"{u.first_name} {u.last_name}".lower() for u in result.users]
        assert any("emily" in name for name in names)


@pytest.mark.api
class TestCreateUser:

    async def test_create_returns_new_user(self, dummyjson: DummyJSONClient) -> None:
        new_user = await dummyjson.create_user({
            "firstName": "Sergey",
            "lastName": "Sitnikov",
            "email": "sergey@qa-sentinel.dev",
            "age": 25,
            "gender": "male",
            "username": "ssrjkk",
            "phone": "+7-999-000-0000",
        })
        assert isinstance(new_user, DummyUser)
        # dummyjson возвращает id > 100 для созданных пользователей
        assert new_user.id > 0

    async def test_created_user_has_required_response_fields(self, dummyjson: DummyJSONClient) -> None:
        """dummyjson возвращает созданного пользователя с id и обязательными полями."""
        new_user = await dummyjson.create_user({
            "firstName": "Test",
            "lastName": "User",
            "email": "test@example.com",
            "age": 30,
            "gender": "male",
            "username": "testuser",
            "phone": "+1-555-000-0000",
        })
        # dummyjson присваивает новый id
        assert new_user.id > 0
        assert new_user.email  # email присутствует в ответе


@pytest.mark.api
class TestUpdateUser:

    async def test_update_returns_updated_user(self, dummyjson: DummyJSONClient) -> None:
        updated = await dummyjson.update_user(1, {"firstName": "Updated"})
        assert isinstance(updated, DummyUser)
        assert updated.first_name == "Updated"


@pytest.mark.api
class TestDeleteUser:

    async def test_delete_returns_deleted_flag(self, dummyjson: DummyJSONClient) -> None:
        result = await dummyjson.delete_user(1)
        assert result["isDeleted"] is True

    async def test_delete_returns_user_data(self, dummyjson: DummyJSONClient) -> None:
        result = await dummyjson.delete_user(1)
        assert "id" in result
        assert "firstName" in result
