from fastapi import APIRouter, Depends, HTTPException
from models import usuarios
from dependences import pegar_sessao
from main import bcrypt_context
from schemas import usuarioSchema
from sqlalchemy.orm import Session


auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def home ():
    """
    Essa é a rota padrao para autenticação da API
    """
    return {"mensagem": "Você acessou a rota padrão de autenticação"}


@auth_router.post("/criar-conta")                  
async def criar_conta(usuario_schemas: usuarioSchema, session: Session = Depends(pegar_sessao)):
    usuario = session.query(usuarios).filter(usuarios.email == usuario_schemas.email). first()
    if usuario:
        #ja existe um usuario com esse email
        #return {"mensagem": "Ja existe um usuario com esse email"}
        raise HTTPException (status_code=400, detail= "Ja existe um usuario com esse email")
    else:
        #criptografar senha
        senha_criptografada = bcrypt_context.hash(usuario_schemas.senha)

        #caso nao exista
        novo_usuario = usuarios(usuario_schemas.nome, usuario_schemas.email, senha_criptografada, usuario_schemas.ativo, usuario_schemas.admin)

        #adicionar novo usuario ao BD
        session.add(novo_usuario)

        #salvar as alterações
        session.commit()
        raise HTTPException (status_code= 200, detail= f"Novo usuario cadastrado com sucesso {novo_usuario.email}")
