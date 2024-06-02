import httpx

from abc import ABC, abstractmethod
from typing import Any

class ControllerConsumerService(ABC):

    def __init__(self, service_route:str, content:str):
        self._service_route = service_route
        self._content = content
    
    @abstractmethod
    async def execute(self)->dict:
        pass

class ControllerConsumerServiceGETMethod(ControllerConsumerService):
        
    async def execute(self):
        headers = {
            'Authorization': self._content
        }
        
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(self._service_route, headers=headers)
                response.raise_for_status()  # Raise HTTPStatusError for bad responses (4xx and 5xx)
                return response.json()  # Assuming the response is JSON and contains the boolean result
            except httpx.HTTPStatusError as e:
                if e.response.status_code == 401:
                    raise ValueError("Token invalido")
                else:
                    raise e
        
class ControllerConsumerServicePOSTMethod(ControllerConsumerService):
    pass