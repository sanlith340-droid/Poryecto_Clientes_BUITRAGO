from fastapi import FastAPI, HTTPException
from pydantic import BaseModel 

app = FastAPI()


#**crear el modelo clientes(id, nombre, email, descripcion)** #Mayuscula incial para class
class Cliente(BaseModel): 
    id: int
    nombre: str
    email: str
    descripcion: str
    
#variables lista de clientes
lista_clientes:list[Cliente] = [
    
]

#endpoint de inicio / para lisar todos los clientes 


#x=12 - init <- creacion de variable y su tipo de dato
#x=ana - str

#get: obtener o listar

@app.get("/clientes")
def listar_clientes():
    return  lista_clientes

#endpoint / para lisar un solo cliente  de la lista

@app.get("/clientes{cliente_id}")
def listar_clientes(cliente_id: int):
    
    #recorrer la lista clientes
    for i , obj_cliente in enumerate (lista_clientes):
        if obj_cliente.get("id") == cliente_id:
            return  obj_cliente 
        
#
#endpoint / para crear  un cliente, y agregar a la lista
@app.post("/clientes/")
def crear_cliente(datos_cliente: Cliente):
    lista_clientes.append(datos_cliente)
    return datos_cliente