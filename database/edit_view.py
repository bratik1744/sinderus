import sqlite3


def edit_view(telegram_id_who: int, telegram_id_whom: int) -> None:
    try:
        con = sqlite3.connect("database/bottind.db")
    except BaseException:
        con = sqlite3.connect("bottind.db")
    cur = con.cursor()
    result = list(cur.execute(f"""SELECT * FROM accounts WHERE "telegram_id" = {telegram_id_who}"""))[0][-1]
    if str(result) != "None":
        result = str(result) + " " + str(telegram_id_whom)
    else:
        result = str(telegram_id_whom)
    cur.execute(f"""UPDATE accounts SET viewed = '{result}' WHERE telegram_id = {telegram_id_who}""")
    con.commit()
    con.close()


if __name__ == "__main__":
    edit_view(123, 125)
