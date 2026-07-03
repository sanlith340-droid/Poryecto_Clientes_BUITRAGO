from fastapi import APIRouter , HTTPException , status

#from app.modelos.clientes import Cliente, ClienteCrear, ClienteEditar
from ..modelos.clientes import Cliente , ClienteCrear , ClienteEditar 
from ..listas import lista_clientes
from ..conexion_bd import sesion_dependencia
from sqlmodel import select



rutas_clientes = APIRouter()

#lista_clientes: list[Cliente] =[]

#endpoint de inicio / para lisar todos los clientes 

@rutas_clientes.get("/clientes",response_model=list[Cliente])
async def listar_clientes(sesion: sesion_dependencia):
    lista_cli = sesion.exec(select(Cliente)).all()
    return  lista_cli
#endpoint / para lisar un solo cliente  de la lista

async def ListarCliente(cliente_id: int, mi_sesion: sesion_dependencia):
    cliente_bd = mi_sesion.get(Cliente, cliente_id)
    if not cliente_bd:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Cliente con id {cliente_id} no encontrado"
        )
    return cliente_bd
        
#
#endpoint / para crear  un cliente, y agregar a la lista
@rutas_clientes.post("/clientes",response_model=Cliente)
async def crear_cliente(datos_cliente: ClienteCrear , mi_sesion: sesion_dependencia):
    cliente_val = Cliente.model_validate(datos_cliente.model_dump())
    mi_sesion.add(cliente_val)
    mi_sesion.commit()
    mi_sesion.refresh(cliente_val)
    return cliente_val

#endpoint / para crear  un cliente, y agregar a la lista
@rutas_clientes.patch("/clientes/{cliente_id}",response_model=Cliente)
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
@rutas_clientes.delete("/clientes/{cliente_id}",response_model=Cliente)    
async def eliminar_cliente(cliente_id: int):
    for i , obj_cliente in enumerate (lista_clientes):
        if obj_cliente.id == cliente_id:
            cliente_eliminado = lista_clientes.pop(i)
            return cliente_eliminado
    raise HTTPException(status_code=400, detail=f"El cliente con id {cliente_id} , no existe")