import pytest

@pytest.mark.game
def test_player_initial_hp(default_player_stats):
    """Game-тест: Проверяет соответствие данных в фикстуре ожидаемым."""
    assert default_player_stats["hp"] == 100

@pytest.mark.game
@pytest.mark.parametrize ("level, expected_hp", [
    (1, 100),
    (5, 150),
    (10, 210)
])

def test_player_hp_by_level (level, expected_hp):
    """Game-тест: Расчет HP."""
    calculated_hp = 100 + (level - 1) * 10
    assert calculated_hp == expected_hp
