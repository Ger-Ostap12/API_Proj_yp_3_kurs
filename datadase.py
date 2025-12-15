"""Простые вспомогательные функции для работы с таблицей ``weather_data``."""

import psycopg2


def _get_connection():
    """Создает подключение к БД с автокоммитом."""
    conn = psycopg2.connect(
        dbname="laba",
        user="postgres",
        password="0508",
        host="localhost",
        port="5432",
    )
    conn.autocommit = True
    return conn


def db_select(table):
    """Выводит в stdout все строки указанной таблицы.

    Args:
        table (str): Имя таблицы базы данных.
    """
    with _get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(f"SELECT * FROM {table}")
            print(cur.fetchall())


def db_create(data):
    """Добавляет запись о погоде в таблицу ``weather_data``.

    Args:
        data (dict): Данные о погоде из API weatherbit.
    """
    with _get_connection() as conn:
        with conn.cursor() as cur:
            try:
                cur.execute(
                    f"""
                        INSERT INTO weather_data
                        (temperature, city, cloudiness, humidity, pressure, wind_speed, wind_direction)
                        VALUES (
                    {data['temp']},
                '{data['city_name']}',
                '{data['clouds']}',
                {data['rh']},
                {data['pres']},
                {data['wind_spd']},
                '{data['wind_cdir_full']}'
                                            )
                                                """
                )
                print("успешное сохранение в БД!!!")
            except Exception as e:
                print(e)


def db_delete(city):
    """Удаляет записи о городе из таблицы ``weather_data``.

    Args:
        city (str): Название города.
    """
    with _get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(f"""DELETE FROM weather_data WHERE city = '{city}'""")
            print(f"запись с {city} удалена")
