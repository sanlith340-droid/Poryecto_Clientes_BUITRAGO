from fastapi import FastAPI
from pydantic import BaseModel
from sqlmodel import SQLModel , field , relationship

#**crear el modelo clientes(id, nombre, email, descripcion)** #Mayuscula incial para class

#seguridad a los modelos de datos

class ClienteBase(SQLModel): 
    nombre: str = field(default=None)
    email: str  = field(default=None)
    descripcion: str | None = field(default=None)
    
class ClienteCrear(ClienteBase):
    pass

class ClienteEditar(ClienteBase):
    pass
    
class Cliente(ClienteBase, table=True):
    id: int | None = field(default=None, primary_key=True)