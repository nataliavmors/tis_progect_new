from flask import Flask, render_template
from back import Films_Data

app = Flask(__name__)
bd = Films_Data()

@app.route("/persons")
def persons():
#Обрабатывает запрос к странице со списком авторов http://mipt-space-tis.ru:5013/ """
    persons_list = bd.get_all_persons()
    ret = render_template("persons.html",persons_list=persons_list)
    return ret

@app.route("/person/<person_id>")
def person(person_id=None):
#"""Обрабатывает запрос к странице конретного автора http://mipt-space-tis.ru:5013/person """
    person_name = bd.get_person(person_id)
    countries = bd.get_person_countries(person_id)
    job = bd.get_person_roles(person_id)
    ret = render_template("person.html", person_name = person_name, countries = countries, films = job)
    return ret

@app.route("/films")
def films():
    films_list = bd.get_all_films()
    ret = render_template("films.html",films_list=films_list)
    return ret

@app.route("/")
def start():
    ret = render_template("start.html")
    return ret


@app.route("/film/<film_id>")
def film(film_id=None):
    film_name = bd.get_film(film_id)
    genres = bd.get_film_genres(film_id)
    countries = bd.get_film_countries(film_id)
    person_list = bd.get_film_persons(film_id)
    ret = render_template("film.html", countries = countries, person_list = person_list, genres = genres, film_name=film_name)
    return ret
    
app.run(host='0.0.0.0',port=6021)