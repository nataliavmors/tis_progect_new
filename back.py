from sqlalchemy import create_engine, text
class Films_Data(object):

    def __init__(self):
        self._engine=create_engine("sqlite:///films.db", echo = True)

    def get_person(self):
    # Возвращает список словарей с информацией по персонам с их id, name, birth, и death
        sql = text("SELECT person.id AS id, person.person_name as name, person.birth_date AS birth, death.death_date AS death FROM person LEFT JOIN death ON person.id = death.dead_person_id;")
        sql_result = self._engine.execute(sql)
        ret = []
        for record in sql_result:
            ret.append(dict(record))
        return ret

    def get_person_countries(self, person_id):
    #Возвращает строку со списком стран принадлежности автора по его id
        sql = text("SELECT GROUP_CONCAT(countries.country_name, \", \") AS Countries FROM person_country JOIN countries ON person_country.country_id = countries.id WHERE person_country.person_id = " + str(person_id) +" ;")
        sql_result = self._engine.execute(sql)
        for record in sql_result:
            dictionary = dict(record)
        return dictionary["Countries"]

    def get_film(self,film_id):
    # Возвращает список словарей с информацией по фильмам с их id, name, release
        sql = text("SELECT film.id AS id, film.film_name AS name, film.release_date AS release FROM film WHERE film.id=" + str(film_id) +";")
        sql_result = self._engine.execute(sql)
        ret = []
        for record in sql_result:
            ret.append(dict(record))
        return ret

    def get_film_countries(self, film_id):
    #Возвращает строку со списком стран принадлежности фильма по его id
        sql = text("SELECT GROUP_CONCAT(countries.country_name, \", \") AS Countries_films FROM film_country JOIN countries ON film_country.country_id = countries.id WHERE film_country.film_id = " + str(film_id) +" ;")
        sql_result = self._engine.execute(sql)
        for record in sql_result:
            dictionary = dict(record)
        return dictionary["Countries_films"]

    def get_film_genres(self, film_id):
    #Возвращает строку со списком жанров фильма по его id
        sql = text("SELECT GROUP_CONCAT(genre.genre_name, \", \") AS Genres FROM film_genre JOIN genre ON film_genre.genre_id = Genre.id WHERE film_genre.film_id = " + str(film_id) +" ;")
        sql_result = self._engine.execute(sql)
        for record in sql_result:
            dictionary = dict(record)
        return dictionary["Genres"]

    def get_person_roles(self,person_id):
        #sql=text("SELECT film_person_role.role_id AS role, film_person_role.film_id AS film FROM film_person_role WHERE film_person_role.person_id = " + str(person_id) + ";")
        sql=text("SELECT roles.role_name , film.film_name FROM film JOIN film_person_role ON film_person_role.film_id=film.id JOIN roles ON film_person_role.role_id=roles.id  WHERE film_person_role.person_id = " + str(person_id) + ";")
        sql_result = self._engine.execute(sql)
        ret=[]
        for record in sql_result:
            ret.append(dict(record))
        return ret

    def get_film_persons(self,film_id):
        sql=text("SELECT roles.role_name , person.person_name FROM person JOIN film_person_role ON film_person_role.person_id=person.id JOIN roles ON film_person_role.role_id=roles.id  WHERE film_person_role.film_id = " + str(film_id) + ";")
        sql_result = self._engine.execute(sql)
        ret=[]
        for record in sql_result:
            ret.append(dict(record))
        return ret

    def get_all_films(self):
        sql = text("SELECT film.id, film.film_name FROM film ORDER BY film_name")
        sql_result = self._engine.execute(sql)
        ret = []
        for record in sql_result:
            ret.append(dict(record))
        return ret

    def get_all_persons(self):
        sql = text("SELECT person.id, person.person_name from person ORDER BY person_name")
        sql_result = self._engine.execute(sql)
        ret = []
        for record in sql_result:
            ret.append(dict(record))
        return ret


#bd = Films_Data()
#print(bd.get_person())
#print()
#print(bd.get_person_roles(1))
#print()
#rint(bd.get_film_persons(1))
#print(bd.get_film_persons(3))
#print(bd.get_all_films())
#print(bd.get_all_persons())
#print (bd.get_person_countries(1))
#print()
#print (bd.get_person_countries(10))
#print()
#print(bd.get_film(1))
#print()
#print (bd.get_film_countries(1))
#print()
#print (bd.get_film_countries(4))
#print()
#print (bd.get_film_genres(1))
#print()
#print (bd.get_film_genres(4))