import sqlite3


def sql_create():
    global db, cursor
    db = sqlite3.connect("bot.sqlite3")
    cursor = db.cursor()

    if db:
        print('База данных подключена!')
    # cursor.execute("DROP TABLE IF EXISTS users")
    # cursor.execute("DROP TABLE IF EXISTS grups")
    db.execute("CREATE TABLE IF NOT EXISTS users"
               "(id INTEGER PRIMARY KEY, user_id INTEGER UNIQUE, name CHAR)")
    db.execute("CREATE TABLE IF NOT EXISTS grups"
               "(id INTEGER PRIMARY KEY, group_id INTEGER UNIQUE, title CHAR)")
    db.commit()


async def sql_command_insert_users(user_id, name):
    cursor.execute("INSERT OR IGNORE INTO users (user_id, name) VALUES (?, ?)", (user_id, name))
    db.commit()


async def sql_command_insert_groups(group_id, title):
    cursor.execute("INSERT OR IGNORE INTO grups (group_id, title) VALUES (?, ?)", (group_id, title))
    db.commit()


async def sql_command_all_users():
    results = cursor.execute("SELECT user_id FROM users").fetchall()
    user_ids = [row[0] for row in results]
    return user_ids


async def sql_command_all_users_name():
    results = cursor.execute("SELECT name FROM users").fetchall()
    user_names = [row[0] for row in results]
    return user_names


async def sql_command_all_groups():
    results = cursor.execute("SELECT group_id FROM grups").fetchall()
    groups_ids = [row[0] for row in results]
    return groups_ids


async def sql_command_all_groups_title():
    results = cursor.execute("SELECT title FROM grups").fetchall()
    groups_titles = [row[0] for row in results]
    return groups_titles


async def sql_command_delete_users(name):
    cursor.execute("DELETE FROM users WHERE name = ?", (name,))
    db.commit()


async def sql_command_delete_groups(title):
    cursor.execute("DELETE FROM grups WHERE title = ?", (title,))
    db.commit()

