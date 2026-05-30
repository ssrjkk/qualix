"""Тесты Products API — dummyjson.com/products"""

from __future__ import annotations

import pytest

from app.external.dummyjson import DummyJSONClient, DummyProduct, ProductsResponse


@pytest.mark.api
class TestGetProducts:
    async def test_returns_products_response(self, dummyjson: DummyJSONClient) -> None:
        result = await dummyjson.get_products()
        assert isinstance(result, ProductsResponse)
        assert result.total > 0
        assert len(result.products) > 0

    async def test_products_have_required_fields(self, dummyjson: DummyJSONClient) -> None:
        result = await dummyjson.get_products()
        for p in result.products:
            assert p.id > 0
            assert p.title
            assert p.price > 0
            assert p.category

    async def test_price_is_positive(self, dummyjson: DummyJSONClient) -> None:
        result = await dummyjson.get_products()
        for p in result.products:
            assert p.price > 0, f"Product {p.id} has non-positive price: {p.price}"

    async def test_rating_in_valid_range(self, dummyjson: DummyJSONClient) -> None:
        result = await dummyjson.get_products()
        for p in result.products:
            assert 0.0 <= p.rating <= 5.0, f"Product {p.id} rating {p.rating} out of range"

    async def test_discount_percentage_in_range(self, dummyjson: DummyJSONClient) -> None:
        result = await dummyjson.get_products()
        for p in result.products:
            assert 0.0 <= p.discount_percentage <= 100.0

    async def test_stock_non_negative(self, dummyjson: DummyJSONClient) -> None:
        result = await dummyjson.get_products()
        for p in result.products:
            assert p.stock >= 0

    async def test_pagination_limit(self, dummyjson: DummyJSONClient) -> None:
        result = await dummyjson.get_products(limit=2)
        assert len(result.products) <= 2


@pytest.mark.api
class TestGetProductById:
    async def test_get_existing_product(self, dummyjson: DummyJSONClient) -> None:
        product = await dummyjson.get_product(1)
        assert isinstance(product, DummyProduct)
        assert product.id == 1

    async def test_product_description_not_empty(self, dummyjson: DummyJSONClient) -> None:
        product = await dummyjson.get_product(1)
        assert len(product.description) > 0

    async def test_discounted_price_less_than_original(self, dummyjson: DummyJSONClient) -> None:
        """Бизнес-правило: цена со скидкой < оригинальной цены."""
        product = await dummyjson.get_product(1)
        if product.discount_percentage > 0:
            discounted = product.price * (1 - product.discount_percentage / 100)
            assert discounted < product.price


@pytest.mark.api
class TestGetProductsByCategory:
    async def test_returns_products_in_category(self, dummyjson: DummyJSONClient) -> None:
        result = await dummyjson.get_products_by_category("beauty")
        assert isinstance(result, ProductsResponse)
        assert len(result.products) > 0

    async def test_all_products_match_category(self, dummyjson: DummyJSONClient) -> None:
        result = await dummyjson.get_products_by_category("beauty")
        for p in result.products:
            assert p.category == "beauty"


@pytest.mark.api
class TestSearchProducts:
    async def test_search_returns_results(self, dummyjson: DummyJSONClient) -> None:
        result = await dummyjson.search_products("phone")
        assert isinstance(result, ProductsResponse)

    async def test_search_total_consistent(self, dummyjson: DummyJSONClient) -> None:
        result = await dummyjson.search_products("phone")
        assert result.total >= len(result.products)
