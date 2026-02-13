from sqlalchemy.orm import sessionmaker
from models import db


def pegar_sessao():
    try:
        Session = sessionmaker(bind= db)
        session = Session()

        #yeld retorna um valor igual o return, porém nao encerra a funcao
        yield session
    
    #executa o fechamento da sessao independente do que acontece no try
    #garantir que a sessao seja fechada no final
    finally:
        session.close()