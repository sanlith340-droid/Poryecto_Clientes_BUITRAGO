from fastapi import FastAPI
from pydantic import BaseModel

#**crear el modelo clientes(id, nombre, email, descripcion)** #Mayuscula incial para class

#seguridad a los modelos de datos

class ClienteBase(BaseModel): 
    nombre: str
    email: str
    descripcion: str
    
class ClienteCrear(ClienteBase):
    pass

class ClienteEditar(ClienteBase):
    pass
    
class Cliente(ClienteBase):
    id: int | None = None 