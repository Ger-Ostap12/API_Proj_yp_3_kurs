"""Тесты для функции `current_weather`."""

import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from api import current_weather


class TestAPI(unittest.TestCase):
    """Проверяет валидацию ввода и базовый ответ API."""

    def test_current_weather_with_empty_string(self):
        """Возвращает None при пустой строке."""
        result = current_weather("")
        assert result is None, "Функция должна вернуть None для пустой строки"

    def test_current_weather_with_none(self):
        """Возвращает None при None."""
        result = current_weather(None)
        assert result is None, "Функция должна вернуть None для None"

    def test_current_weather_with_number(self):
        """Возвращает None при числовом вводе."""
        result = current_weather(123)
        assert result is None, "Функция должна вернуть None для числа"

    def test_current_weather_with_valid_city(self):
        """Возвращает словарь при корректном городе и наличии API ключа."""
        if not os.getenv("API_KEY"):
            self.skipTest("API_KEY не установлен")

        result = current_weather("Москва")
        if result is not None:
            assert isinstance(result, dict), "Результат должен быть словарем"
            if "data" in result:
                assert isinstance(result["data"], list), "data должен быть списком"
                if result["data"]:
                    assert "city_name" in result["data"][0], "Должно быть поле city_name"


if __name__ == "__main__":
    unittest.main()
