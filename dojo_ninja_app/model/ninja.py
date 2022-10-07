from dojo_ninja_app.config.mysqlconnection import connectToMySQL
from dojo_ninja_app.model import dojo


class Ninja:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at  = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO ninjas (dojo_id,first_name, last_name, age, created_at, updated_at)"
        query += " VALUES(%(dojo_id)s,%(first_name)s, %(last_name)s, %(age)s, NOW(), NOW());"
        return connectToMySQL('dojo_ninja').query_db(query,data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL('dojo_ninja').query_db(query)

        ninjas = []

        for ninja in results:
            ninjas.append(cls(ninja))
        return ninjas