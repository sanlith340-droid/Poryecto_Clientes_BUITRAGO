from fastapi import FastAPI, HTTPException
from modelos.clientes import Cliente, ClienteCrear

app = FastAPI()



    
#variables lista de clientes
lista_clientes:list[Cliente] = [
    
]

#endpoint de inicio / para lisar todos los clientes 


#x=12 - init <- creacion de variable y su tipo de dato
#x=ana - str

#get: obtener o listar

@app.get("/clientes",response_model=list[Cliente])
def listar_clientes():
    return  lista_clientes

#endpoint / para lisar un solo cliente  de la lista

@app.get("/clientes{cliente_id}",response_model=Cliente)
def listar_clientes(cliente_id: int):
    
    #recorrer la lista clientes
    for i , obj_cliente in enumerate (lista_clientes):
        if obj_cliente.get("id") == cliente_id:
            return  obj_cliente 
        
#
#endpoint / para crear  un cliente, y agregar a la lista
@app.post("/clientes",response_model=Cliente)
def crear_cliente(datos_cliente: ClienteCrear):
    cliente_val = Cliente.model_validate(datos_cliente.model_dump())
    lista_clientes.append(cliente_val)
    return cliente_val