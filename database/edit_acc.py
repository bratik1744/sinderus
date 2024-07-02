import sqlite3


def edit_acc(telegram_id: int, name: str = None, old: int = None, gender: str = None,
              direction: str = None, description: str = None, gender_interests: str = None,
              id_last_commands: int = None, completed: int = None, id_like: int = None) -> None:
    # Открываем соединение с базой данных
    try:
        con = sqlite3.connect("database/bottind.db")
    except BaseException:
        con = sqlite3.connect("bottind.db")

    cur = con.cursor()

    query = "UPDATE accounts SET "
    updates = []
    if name is not None:
        updates.append(f"name = '{name}'")
    if old is not None:
        updates.append(f"old = {old}")
    if gender is not None:
        updates.append(f"gender = '{gender}'")
    if completed is not None:
        updates.append(f"completed = {completed}")

    if direction is not None:
        updates.append(f"direction = '{direction}'")
    if description is not None:
        updates.append(f"description = '{description}'")
    if gender_interests is not None:
        updates.append(f"gender_interests = '{gender_interests}'")
    if id_last_commands is not None:
        updates.append(f"id_last_commands = {id_last_commands}")
    if id_like is not None:
        updates.append(f"id_like = {id_like}")
    if len(updates) > 0:
        query += ", ".join(updates)
        query += f" WHERE telegram_id = {telegram_id}"
        cur.execute(query)

    # Закрываем соединение с базой данных
    con.commit()
    con.close()

if __name__ == "__main__":
    edit_acc(telegram_id=123, gender="f")