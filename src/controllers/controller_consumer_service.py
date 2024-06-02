import httpx

from abc import ABC, abstractmethod
from typing import Any

class ControllerConsumerService(ABC):

    def __init__(self, service_route:str, content):
        self._service_route = service_route
        self._content = content
    
    @abstractmethod
    async def execute(self)->dict:
        pass

class ControllerConsumerServiceGETMethod(ControllerConsumerService):

    async def execute(self) -> Any:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{self._service_route}/{self._content}")
            response.raise_for_status()
            return response.json()
        
class ControllerConsumerServicePOSTMethod(ControllerConsumerService):
    pass