import sqlite3


def search_anket(gender: str = None) -> list:
    try:
        con = sqlite3.connect("database/bottind.db")
    except BaseException:
        con = sqlite3.connect("bottind.db")
    cur = con.cursor()
    if gender is not None:
        result = list(cur.execute(f"""SELECT * FROM accounts WHERE gender = '{gender}' and completed = 1"""))
    else:
        result = list(cur.execute(f"""SELECT * FROM accounts WHERE completed = 1"""))
    con.close()
    return result


if __name__ == "__main__":
    print(search_anket())