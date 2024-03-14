from redis import Redis
from .utilities import REDIS_PORT, REDIS_HOST, REDIS_PASSWORD
import ast
import json

class Cache:
    _instance = None  
    redis = Redis(
        host=REDIS_HOST,
        port=REDIS_PORT, 
        # password=REDIS_PASSWORD,
    )
    
    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Cache, cls).__new__(cls)
        return cls._instance
        
    def get(self, name): 
        raw_data = self.redis.get(name)
        
        if not raw_data: return None
        
        return raw_data.decode()
        
    def dget(self, name):
        raw_data = self.redis.get(name)
        if not raw_data: return None
        raw_data =  raw_data.decode()
        data = json.loads(raw_data)

        return data

    def set(self, name, value, exp=86400): #? default expiring time is 24 hours
        if exp: self.redis.set(name, value, exp)
        else: self.redis.set(name, value)
        
    def dset(self, name, data, exp=None):
        raw_data = json.dumps(data)
        
        if exp: self.redis.set(name, raw_data, exp)
        else: self.redis.set(name, raw_data)
        
        
    def mset(self, data): self.redis.mset(data)
        
    def delete(self, name): self.redis.delete(name)