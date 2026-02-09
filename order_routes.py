from fastapi import APIRouter

order_router = APIRouter(prefix="/pedidos", tags=["pedidos"])

@order_router.get("/")
async def pedidos():
    """
    Essa é a rota padrao de pedidos da API
    """
    return {"Mensagem": "Você acessou a rota de pedidos"}