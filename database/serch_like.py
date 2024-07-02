import sqlite3


def search_like(telegram_id_who: int, telegram_id_whom: int = None) -> list:
    try:
        con = sqlite3.connect("database/bottind.db")
    except BaseException:
        con = sqlite3.connect("bottind.db")
    cur = con.cursor()
    if telegram_id_whom is not None:
        result = list(cur.execute(f"""SELECT * FROM liked WHERE "telegram_id_who" = {telegram_id_who} and "telegram_id_whom" = {telegram_id_whom}"""))
    else:
        result = list(cur.execute(
            f"""SELECT * FROM liked WHERE "telegram_id_who" = {telegram_id_who}"""))
    con.close()

    return result



if __name__ == "__main__":
    print(search_like(123, 125))