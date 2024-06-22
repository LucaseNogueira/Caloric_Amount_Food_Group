import httpx

from abc import ABC, abstractmethod
from typing import Any

class ControllerConsumerService(ABC):

    def __init__(self, service_route:str, content:str):
        self._service_route = service_route
        self._content = content
    
    @abstractmethod
    def execute(self)->dict:
        pass

class ControllerConsumerServiceGETMethod(ControllerConsumerService):
    
    def execute(self):
        headers = {
            'Authorization': 'Bearer ' + self._content
        }
        
        with httpx.Client() as client:
            try:
                response = client.get(self._service_route, headers=headers)
                response.raise_for_status()
                return response.json()  # Assuming the response is JSON and contains the boolean result
            except httpx.HTTPStatusError as e:
                if e.response.status_code == 401:
                    raise ValueError("Token invalido")
                else:
                    raise e
        
class ControllerConsumerServicePOSTMethod(ControllerConsumerService):
    pass