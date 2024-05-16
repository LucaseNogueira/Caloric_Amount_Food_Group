from pydantic import BaseModel
from typing import List, Optional

class AlimentoRequest(BaseModel):

    descricao: str
    porcao: Optional[float] = 100.0

class AlimentoRequestList(BaseModel):
    alimentos: List[AlimentoRequest]