"""Пакет для получения и сохранения данных о погоде.

Экспортирует функции для запроса актуальных метеоданных, запуска CLI и
сохранения результатов в разные форматы.
"""

from .api import current_weather
from .main import main
from .save import save_json, save_txt

__all__ = [
    "current_weather",
    "main",
    "save_json",
    "save_txt",
]
