import csv
import json
from bottle import route, run, template
from peewee import SqliteDatabase, Model, CharField, DateField, BooleanField


db = SqliteDatabase('data.db')


class Client(Model):
    email = CharField()
    first_name = CharField()
    last_name = CharField()
    date = DateField()

    class Meta:
        database = db


def get_date_from_file():
    with open("data.csv", "rU") as f:
        reader = csv.DictReader(f)
        lista_dictow = []
        for row in reader:
            lista_dictow.append(row)
        return lista_dictow


@route("/")
def index():
    return json.dumps(get_date_from_file())


if __name__ == '__main__':
    run(host="localhost", port=8080, debug=True)
