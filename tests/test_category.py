import pytest

from src.Category import Category


def test_category_init(category_phone, category_tv):
    assert category_phone.name == "Смартфоны"
    assert (
        category_phone.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )

    assert category_phone.category_count == 2
    assert category_phone.product_count == 4


def test_category_get(category_phone):
    assert category_phone.products == (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n"
    )


def test_category_str(category_phone):
    assert str(category_phone) == "Смартфоны, количество продуктов: 27 шт."


def test_add_prod(category_tv, product_tv):
    Category.product_count = 1
    category_tv.add_product(product_tv)
    assert category_tv.product_count == 2
    with pytest.raises(TypeError):
        category_tv.add_product(3)


def test_middle_price(category_phone):
    assert category_phone.middle_price() == 140_333.33


def test_middle_price_with_empty_category():
    empty_category = Category("Пустая категория", "Категория без продуктов", [])
    assert empty_category.middle_price() == 0
