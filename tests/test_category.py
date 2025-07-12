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
