from fastapi import FastAPI
from pydantic import BaseModel
from sqlmodel import SQLModel , Field , Relationship

#**crear el modelo clientes(id, nombre, email, descripcion)** #Mayuscula incial para class

#seguridad a los modelos de datos

class ClienteBase(SQLModel): 
    nombre: str = Field(default=None)
    email: str  = Field(default=None)
    descripcion: str | None = Field(default=None)
    
class ClienteCrear(ClienteBase):
    pass

class ClienteEditar(ClienteBase):
    pass
    
class Cliente(ClienteBase, table=True):
    id: int | None = Field(default=None, primary_key=True)