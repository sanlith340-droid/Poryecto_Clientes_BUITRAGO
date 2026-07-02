from fastapi import FastAPI, HTTPException
from modelos.clientes import Cliente, ClienteCrear , ClienteEditar

app = FastAPI()



    
#variables lista de clientes
lista_clientes:list[Cliente] = [
    
]

#endpoint de inicio / para lisar todos los clientes 


#x=12 - init <- creacion de variable y su tipo de dato
#x=ana - str

#get: obtener o listar

@app.get("/clientes",response_model=list[Cliente])
async def listar_clientes():
    return  lista_clientes

#endpoint / para lisar un solo cliente  de la lista

@app.get("/clientes{cliente_id}",response_model=Cliente)
async def listar_clientes(cliente_id: int):
    
    #recorrer la lista clientes
    for i , obj_cliente in enumerate (lista_clientes):
        if obj_cliente.id == cliente_id:
            return  obj_cliente 
        
#
#endpoint / para crear  un cliente, y agregar a la lista
@app.post("/clientes",response_model=Cliente)
async def crear_cliente(datos_cliente: ClienteCrear):
    cliente_val = Cliente.model_validate(datos_cliente.model_dump())
    #generar id
    id_cliente = len(lista_clientes)+1
    cliente_val.id = id_cliente
    lista_clientes.append(cliente_val)
    return cliente_val

#endpoint / para crear  un cliente, y agregar a la lista
@app.patch("/clientes/{cliente_id}",response_model=Cliente)
async def editar_cliente(cliente_id: int, datos_cliente: ClienteEditar):
    for i , obj_cliente in enumerate (lista_clientes):
        if obj_cliente.id == cliente_id:
            #validar cliente
            cliente_val = Cliente.model_validate(datos_cliente.model_dump())
            cliente_val.id = cliente_id
            lista_clientes[i] = cliente_val
            return  cliente_val
        raise HTTPException(status_code=400, detail=f"El cliente con id {cliente_id} , no existe")

#endpoint / para eliminar  un cliente, y agregar a la lista
@app.delete("/clientes/{cliente_id}",response_model=Cliente)    
async def eliminar_cliente(cliente_id: int):
    for i , obj_cliente in enumerate (lista_clientes):
        if obj_cliente.id == cliente_id:
            return  lista_clientes.pop(i)
    raise HTTPException(status_code=400, detail=f"El cliente con id {cliente_id} , no existe")