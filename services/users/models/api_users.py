import requests
from utils.helper import Helper
from models.endpoints import Endpoints
from models.payloads import Payloads
from config.headers import Headers


class UserAPI(Helper):
    def __init__(self):
        super().__init__()
        self.endpoints = Endpoints()
        self.header = Headers()
        self.payload = Payloads()

    def create_users(self):
            
        response = requests.post(
            url = self.endpoints.create_user,
            headers= self.header.basic,
            json = self.payload.create_user
        )
        print(response.json)
        assert response.status_code == 200
        
        