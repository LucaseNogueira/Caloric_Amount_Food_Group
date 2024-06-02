from fastapi import FastAPI, Depends
from src.models.alimento_request import AlimentoRequestList
from src.controllers.controller_calorias_grupo_alimento_route import ControllerCaloriasGrupoAlimentoRoute
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

# Define o esquema OAuth2 com Bearer Token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.post('/foodgroup/')
async def get_calorias_por_grupo_alimentos(alimentos:AlimentoRequestList, token: str = Depends(oauth2_scheme)):
    controller = ControllerCaloriasGrupoAlimentoRoute(alimentos, token)
    return controller.execute()