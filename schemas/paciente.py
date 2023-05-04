from pydantic import BaseModel
from typing import Optional, List
from model.paciente import Paciente

from schemas import ComentarioSchema


class PacienteSchema(BaseModel):
    """ Define como um novo paciente a ser inserido deve ser representado
    """
    nome: str = "Nome do Paciente:"
    telefone: str = "(xx) xxxxx-xxxx"
    data_consulta: str = "dd/mm/aaaa"
    hora: str = "mm:hh"
    tipo: str = "Consulta ou Retorno"


class PacienteBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do paciente.
    """
    nome: str = "Teste"


class ListagemPacientesSchema(BaseModel):
    """ Define como uma listagem de pacientes será retornada.
    """
    pacientes:List[PacienteSchema]


def apresenta_pacientes(pacientes: List[Paciente]):
    """ Retorna uma representação do paciente seguindo o schema definido em
        PacienteViewSchema.
    """
    result = []
    for paciente in pacientes:
        result.append({
            "nome": paciente.nome,
            "telefone": paciente.telefone,
            "data_consulta": paciente.data_consulta,
            "hora": paciente.hora,
            "tipo": paciente.tipo,
        })

    return {"pacientes": result}


class PacienteViewSchema(BaseModel):
    """ Define como um paciente será retornado: paciente + comentários.
    """
    id: int = 1
    nome: str = "Nome do Paciente"
    telefone: str = "(xx) xxxxx-xxxx" 
    data_consulta: str = "dd/mm/aaaa"
    hora: str = "mm:hh"
    tipo: str = "Consulta ou retorno"
    total_cometarios: int = 1
    comentarios:List[ComentarioSchema]


class PacienteDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    nome: str

def apresenta_paciente(paciente: Paciente):
    """ Retorna uma representação do paciente seguindo o schema definido em
        PacienteViewSchema.
    """
    return {
        "id": paciente.id,
        "nome": paciente.nome,
        "telefone": paciente.telefone,
        "data_consulta": paciente.data_consulta,
        "hora": paciente.hora,
        "tipo": paciente.tipo,
        "total_cometarios": len(paciente.comentarios),
        "comentarios": [{"texto": c.texto} for c in paciente.comentarios]
    }
