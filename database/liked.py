import sqlite3


def new_like(telegram_id_who: int, telegram_id_whom: int) -> None:
    try:
        con = sqlite3.connect("database/bottind.db")
    except BaseException:
        con = sqlite3.connect("bottind.db")
    cur = con.cursor()
    cur.execute(
        f"""INSERT INTO liked("telegram_id_who", "telegram_id_whom") 
        VALUES({telegram_id_who}, {telegram_id_whom});""")
    con.commit()
    con.close()


if __name__ == "__main__":
    new_like(123, 124)
