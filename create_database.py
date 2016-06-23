from peewee import SqliteDatabase
from lesson_1 import Client


def create_database():
    with open('data.db', 'w+') as f:
        f.write('')
    db = SqliteDatabase('data.db')
    db.connect()
    db.create_table(Client)


if __name__ == '__main__':
    create_database()
