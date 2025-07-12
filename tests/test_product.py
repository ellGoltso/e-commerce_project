from src.Product import Product


def test_product_init(product_xiaomi):
    assert product_xiaomi.name == "Xiaomi Redmi Note 11"
    assert product_xiaomi.description == "1024GB, Синий"
    assert product_xiaomi.price == 31000.0
    assert product_xiaomi.quantity == 14


def test_new_product(dict_product):
    new_prod = Product.new_product(dict_product)
    assert new_prod.name == "Samsung Galaxy S23 Ultra"
    assert new_prod.description == "256GB, Серый цвет, 200MP камера"
    assert new_prod.price == 180000.0
    assert new_prod.quantity == 5
