def test_category_init(category_phone, category_tv):
    assert category_phone.name == "Смартфоны"
    assert (
        category_phone.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )

    assert category_phone.category_count == 2
    assert category_phone.product_count == 4
