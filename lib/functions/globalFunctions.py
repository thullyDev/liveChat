import ast
import json
from ..resources.utilities import SUCESSFUL, NOT_FOUND, FORBIDEEN, CRASH, CRASH_MSG, NOT_FOUND_MSG, SUCESSFUL_MSG, FORBIDEEN_MSG

class GlobalFunctions:
    def bad_token(self, data={}) -> dict:
        return self.forbidden(data=data)
        
    def forbidden(self, data={}) -> dict: 
        return self.respond(message=FORBIDEEN_MSG, status_code=FORBIDEEN, data=data)
        
    def successful(self, data={}) -> dict:
        return self.respond(message=SUCESSFUL_MSG, status_code=SUCESSFUL, data=data)
        
    def not_found(self, data={}) -> dict:
        return self.respond(message=NOT_FOUND_MSG, status_code=NOT_FOUND, data=data)
        
    def crash(self, data={}) -> dict:
        return self.respond(message=CRASH_MSG, status_code=CRASH, data=data)
        
    def respond(self, message, status_code, data) -> dict:
        response = {
            "status_code": status_code,
            "message": message, 
            "data": None,
        }
         
        response.update(data)
        
        return response