import sqlite3


def search_acc(telegram_id: int) -> list:
    try:
        con = sqlite3.connect("database/bottind.db")
    except BaseException:
        con = sqlite3.connect("bottind.db")
    cur = con.cursor()
    result = list(cur.execute(f"""SELECT * FROM accounts WHERE telegram_id = {telegram_id}"""))
    con.close()
    return result


if __name__ == "__main__":
    print(search_acc(123))