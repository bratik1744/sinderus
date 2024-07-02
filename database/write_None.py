import sqlite3


def write_None(telegram_id: int) -> None:
    # Открываем соединение с базой данных
    try:
        con = sqlite3.connect("database/bottind.db")
    except BaseException:
        con = sqlite3.connect("bottind.db")

    cur = con.cursor()

    query = f"UPDATE accounts SET gender_interests = Null WHERE telegram_id = {telegram_id}"

    cur.execute(query)

    # Закрываем соединение с базой данных
    con.commit()
    con.close()

if __name__ == "__main__":
    write_None(6835823616)