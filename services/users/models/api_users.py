import requests
from utils.helper import Helper
from services.users.models.endpoints import Endpoints
from payloads import Payloads
from config.headers import Headers



class UserAPI(Helper):
    def __init__(self):
        super().__init__()
        self.endpoints = Endpoints(),
        self.payloads = Payloads(),
        self.headers = Headers()
        

            
    def create_users(self):
        response = requests.post(
            url = self.endpoints,
            headers= self.headers.basic,
            Payloads = self.payloads
        )