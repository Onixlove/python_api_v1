import os

HOST = "https://release-gs.qa-playground.com/api/v1"

class Endpoints:
    
    create_user = f"{HOST}/users"
    get_user_id = lambda self, uuid: f"{HOST}/users/{uuid}"
    