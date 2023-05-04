from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base, Comentario


class Paciente(Base):
    __tablename__ = 'paciente'

    id = Column("pk_paciente", Integer, primary_key=True)
    nome = Column(String(140), unique=True)
    telefone = Column(String(140))
    data_consulta = Column(String(140))
    hora = Column(String(140))
    tipo = Column(String(140))
    data_insercao = Column(DateTime, default=datetime.now())

    # Definição do relacionamento entre o paciente e o comentário.
    # Essa relação é implicita, não está salva na tabela 'paciente',
    # mas aqui estou deixando para SQLAlchemy a responsabilidade
    # de reconstruir esse relacionamento.
    comentarios = relationship("Comentario")

    def __init__(self, nome:str, telefone:str, data_consulta:str, hora:str, tipo:str,
                 data_insercao:Union[DateTime, None] = None):
        """
        Cria um Paciente

        Arguments:
            nome: nome do paciente.
            quantidade: quantidade que se espera comprar daquele paciente
            valor: valor esperado para o paciente
            data_insercao: data de quando o paciente foi inserido à base
        """
        self.nome = nome
        self.telefone = telefone
        self.data_consulta = data_consulta
        self.hora = hora
        self.tipo = tipo

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao

    def adiciona_comentario(self, comentario:Comentario):
        """ Adiciona um novo comentário ao Paciente
        """
        self.comentarios.append(comentario)

