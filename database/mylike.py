import sqlite3


def mylike(telegram_id) -> list:
    try:
        con = sqlite3.connect("database/bottind.db")
    except BaseException:
        con = sqlite3.connect("bottind.db")
    cur = con.cursor()
    result = list(cur.execute(f"""SELECT * FROM liked WHERE "telegram_id_whom" = {telegram_id}"""))
    con.close()
    return result



if __name__ == "__main__":
    print(search_like(123))