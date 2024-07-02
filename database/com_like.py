import sqlite3


def com_like(telegram_id_who: int, telegram_id_whom: int) -> None:
    # Открываем соединение с базой данных
    try:
        con = sqlite3.connect("database/bottind.db")
    except BaseException:
        con = sqlite3.connect("bottind.db")

    cur = con.cursor()

    # Составляем запрос для поиска нужных записей в базе данных

    query = f"""UPDATE liked SET "completed" = 1 
    WHERE "telegram_id_who" = {telegram_id_who} and "telegram_id_whom" = {telegram_id_whom}"""

    cur.execute(query)

    # Закрываем соединение с базой данных
    con.commit()
    con.close()

if __name__ == "__main__":
    com_like(123, 124)