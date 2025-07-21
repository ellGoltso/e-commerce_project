def test_samsung(smartphone_samsung):
    assert smartphone_samsung.name == "Samsung Galaxy S23 Ultra"
    assert smartphone_samsung.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone_samsung.price == 180000.0
    assert smartphone_samsung.quantity == 5
    assert smartphone_samsung.efficiency == 95.5
    assert smartphone_samsung.model == "S23 Ultra"
    assert smartphone_samsung.memory == 256
    assert smartphone_samsung.color == "Серый"
