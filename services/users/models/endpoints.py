import os

HOST = "https://dev-gs.qa-playground.com/api/v1"

class Endpoints:
    
    create_users_777 = f"{HOST}/users"
    get_user_id = lambda self, uuid: f"{HOST}/users/{uuid}"
    