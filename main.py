from fastapi import FastAPI, Depends
from src.models.alimento_request import AlimentoRequestList
from src.controllers.controller_calorias_grupo_alimento_route import ControllerCaloriasGrupoAlimentoRoute
from fastapi.security import OAuth2PasswordBearer
from prometheus_fastapi_instrumentator import Instrumentator
from fastapi.openapi.utils import get_openapi
import os
from dotenv import load_dotenv

load_dotenv()
env = os.getenv("ENV")

app = FastAPI()
Instrumentator().instrument(app).expose(app)

# Define o esquema OAuth2 com Bearer Token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
if env == "dev":
    def custom_openapi():
        openapi_schema = get_openapi(
            title="API Food Group",
            version="1.0.0",
            description="Documentação da Api do Food Group",
            routes=app.routes,
        )
        return openapi_schema

    app.openapi = custom_openapi

@app.post('/foodgroup/',tags=["foodgroup"], summary="Calcula calorias por grupo de alimentos")
async def get_calorias_por_grupo_alimentos(alimentos:AlimentoRequestList, token: str = Depends(oauth2_scheme)):
    controller = ControllerCaloriasGrupoAlimentoRoute(alimentos, token)
    return controller.execute()