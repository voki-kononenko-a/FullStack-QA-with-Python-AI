import pytest

@pytest.mark.game
def test_player_initial_hp(default_player_stats):
    """Game-тест: Проверяет соответствие данных в фикстуре ожидаемым."""
    assert default_player_stats["hp"] == 100
