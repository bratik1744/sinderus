import sqlite3

def new_user(telegram_id: int, username: str) -> None:
    try:
        con = sqlite3.connect("database/bottind.db")
    except BaseException:
        con = sqlite3.connect("bottind.db")
    cur = con.cursor()
    cur.execute(f"""INSERT INTO accounts("telegram_id", "username", "id_last_commands") 
                    VALUES({telegram_id}, "{username}", 0);""")
    con.commit()
    con.close()

if __name__ == "__main__":
    new_user(telegram_id=123)
