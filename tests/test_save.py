"""Тесты для функций сохранения погодных данных."""

import json
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from save import save_json, save_txt


class TestWeatherFunctionsSimple(unittest.TestCase):
    """Проверяет корректность сохранения в JSON и TXT."""

    def test_save_json(self):
        """Сохраняет данные в ``report.json`` и корректно записывает поля."""
        test_data = {
            "city_name": "Тестовый город",
            "temp": 20,
            "app_temp": 22,
            "weather": {"description": "облачно"},
            "rh": 50,
            "pres": 1000,
            "wind_spd": 2.0,
            "wind_cdir_full": "западный",
        }

        save_json(test_data)

        self.assertTrue(os.path.exists("report.json"))

        with open("report.json", "r", encoding="utf-8") as f:
            content = json.load(f)

        self.assertEqual(content["city_name"], "Тестовый город")
        self.assertEqual(content["temp"], 20)

        os.remove("report.json")

    def test_save_txt(self):
        """Сохраняет текстовый отчет в ``report.txt``."""
        test_data = {
            "city_name": "Тестовый город",
            "temp": 20,
            "app_temp": 22,
            "weather": {"description": "облачно"},
            "rh": 50,
            "pres": 1000,
            "wind_spd": 2.0,
            "wind_cdir_full": "западный",
        }

        save_txt(test_data)

        self.assertTrue(os.path.exists("report.txt"))

        with open("report.txt", "r", encoding="utf-8") as f:
            content = f.read()

        self.assertIn("Погода в Тестовый город", content)
        self.assertIn("Температура -- 20°C", content)
        self.assertIn("Облачность -- облачно", content)

        os.remove("report.txt")


if __name__ == "__main__":
    unittest.main()
