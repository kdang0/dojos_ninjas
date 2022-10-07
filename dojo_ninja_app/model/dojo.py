from dojo_ninja_app.config.mysqlconnection import connectToMySQL
from dojo_ninja_app.model import ninja

class Dojo:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name, created_at, updated_at)"
        query += "VALUES (%(dojo_name)s, NOW(), NOW());"
        return connectToMySQL('dojo_ninja').query_db(query,data)

    @classmethod
    def get_dojo_w_ninjas(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON "
        query += "dojos.id = ninjas.dojo_id "
        query += "WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojo_ninja').query_db(query,data)
        if results:
            dojo = cls(results[0])
            for row_db in results:
                ninja_data = {
                    "id" : row_db["ninjas.id"],
                    "first_name" : row_db["first_name"],
                    "last_name" : row_db["last_name"],
                    "age" : row_db["age"],
                    "created_at" : row_db["ninjas.created_at"],
                    "updated_at" : row_db["ninjas.updated_at"]
                }
                dojo.ninjas.append(ninja.Ninja(ninja_data))
            return dojo 
    

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos"
        results = connectToMySQL('dojo_ninja').query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos