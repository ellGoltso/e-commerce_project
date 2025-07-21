def test_grass(grass_fixture):
    assert grass_fixture.name == "Газонная трава"
    assert grass_fixture.description == "Элитная трава для газона"
    assert grass_fixture.price == 500.0
    assert grass_fixture.quantity == 20
    assert grass_fixture.country == "Россия"
    assert grass_fixture.germination_period == "7 дней"
    assert grass_fixture.color == "Зеленый"
