"""Тесты Posts API — dummyjson.com/posts"""
from __future__ import annotations

import pytest
from app.external.dummyjson import DummyJSONClient, DummyPost, PostsResponse


@pytest.mark.api
class TestGetPosts:

    async def test_returns_posts_response(self, dummyjson: DummyJSONClient) -> None:
        result = await dummyjson.get_posts()
        assert isinstance(result, PostsResponse)
        assert result.total > 0

    async def test_posts_have_required_fields(self, dummyjson: DummyJSONClient) -> None:
        result = await dummyjson.get_posts()
        for post in result.posts:
            assert post.id > 0
            assert post.title
            assert post.body
            assert post.user_id > 0

    async def test_posts_have_tags(self, dummyjson: DummyJSONClient) -> None:
        result = await dummyjson.get_posts()
        for post in result.posts:
            assert isinstance(post.tags, list)

    async def test_views_non_negative(self, dummyjson: DummyJSONClient) -> None:
        result = await dummyjson.get_posts()
        for post in result.posts:
            assert post.views >= 0


@pytest.mark.api
class TestGetPostById:

    async def test_get_existing_post(self, dummyjson: DummyJSONClient) -> None:
        post = await dummyjson.get_post(1)
        assert isinstance(post, DummyPost)
        assert post.id == 1

    async def test_post_body_not_empty(self, dummyjson: DummyJSONClient) -> None:
        post = await dummyjson.get_post(1)
        assert len(post.body) > 10


@pytest.mark.api
class TestGetUserPosts:

    async def test_returns_posts_for_user(self, dummyjson: DummyJSONClient) -> None:
        result = await dummyjson.get_user_posts(121)
        assert isinstance(result, PostsResponse)

    async def test_all_posts_belong_to_user(self, dummyjson: DummyJSONClient) -> None:
        result = await dummyjson.get_user_posts(121)
        for post in result.posts:
            assert post.user_id == 121
