from sqlalchemy import create_engine, Column, String, Integer, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy_utils.types import ChoiceType

#criar a conexao do banco de dados
db = create_engine("sqlite:///banco.db")

#criar a base do banco de dados
Base = declarative_base()

#cria as classes/tabelas do banco
class usuarios(Base):
    __tablename__= "usuarios"
    
    id= Column("id", Integer, primary_key= True, autoincrement=True) #primary_key normalmente em IDs/ autoincrement para criar os IDs em sequencia (1, 2,3... )
    name= Column("Name", String)
    email= Column("email", String, nullable= False) #"nullable= False" não deixa criar um user sem o parametro gmail
    senha= Column("senha", String)
    ativo= Column("ativo", Boolean)
    admin= Column("admin", Boolean, default= False) #"defaut= false" deixa criar um user sem o parametro admin

    def __init__(self, name, email, senha, ativo= True, admin=False):
        self.name = name
        self.email = email
        self.senha = senha
        self.ativo = ativo
        self.admin = admin


#pedidos
class pedido(Base):
    __tablename__= "pedidos"

    # STATUS_PEDIDO = (
    #     #(chave, valor)
    #     ("PENDENTE", "PENDENTE"),
    #     ("CANCELADO", "CANCELADO"),
    #     ("FINALIZADO", "FINALIZADO")
    # )

    id = Column("id", Integer, primary_key= True, autoincrement= True)
    status =  Column("status", String) #pendente, cancelado, finalizado
    usuario =  Column("usuario", ForeignKey("usuarios.id"))
    preco =  Column("preco", Float)
    #itens =

    def __init__(self, usuario, status= "Pendente", preco= 0):
        self.usuario = usuario
        self.status = status
        self.preco = preco


#itens
class ItemPedido(Base):
    __tablename__= "itens_pedido"

    # TAMANHO_LANCHE = (
    #     ("Grande", "Grande"),
    #     ("Medio", "Medio"),
    #     ("Pequeno", "Pequeno")
    # )

    id = Column("id", Integer, primary_key= True, autoincrement= True)
    tamanho = Column("tamanho", String)
    nome_lanche = Column("nome_lanche", String)
    quantidade = Column("quantidade", Integer)
    preco_uni = Column("preco_uni", Float)
    pedido = Column("pedido", ForeignKey("pedidos.id"))

    def __init__(self, tamanho, nome_lanche, pedido, quantidade= 1, preco_uni = 0):
        self.tamanho = tamanho
        self.nome_lanche = nome_lanche
        self.quantidade = quantidade
        self.preco_uni = preco_uni
        self.pedido = pedido


#executa a criação dos metadados do banco (cria efetivamente o banco de dados)