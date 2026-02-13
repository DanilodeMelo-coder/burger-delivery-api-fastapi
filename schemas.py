from pydantic import BaseModel
from typing import Optional


class usuarioSchema(BaseModel):
    nome: str
    email: str
    senha: str
    ativo: Optional[bool]
    admin: Optional[bool]

    class config():
        #dizer que essa clase não vai ser interpretada com dicionario e sim como orm em models
        from_attributes = True