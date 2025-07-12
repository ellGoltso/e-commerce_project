import pytest

from src.Category import Category
from src.Product import Product


@pytest.fixture
def product_xiaomi():
    return Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31_000.0, 14)


@pytest.fixture
def category_phone():
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180_000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210_000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31_000.0, 14)
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )


@pytest.fixture
def category_tv():
    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123_000.0, 7)
    return Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [product4],
    )


@pytest.fixture
def dict_product():
    return {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
    }
