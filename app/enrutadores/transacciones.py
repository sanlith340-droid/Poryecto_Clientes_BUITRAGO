from fastapi import APIRouter, HTTPException, status
from ..modelos.transacciones import Transaccion, TransaccionCrear, TransaccionEditar
from ..enrutadores.factura import lista_facturas
from ..listas import lista_facturas , lista_transacciones

rutas_transacciones = APIRouter()

#lista_transacciones: list[Transaccion] = []


# Endpoint para listar todas las transacciones
@rutas_transacciones.get("/transacciones", response_model=list[Transaccion])
async def listar_transacciones():
    return lista_transacciones


# Endpoint para listar una transacción
@rutas_transacciones.get("/transacciones/{id_transaccion}", response_model=Transaccion)
async def listar_transaccion(id_transaccion: int):

    for i, obj_transaccion in enumerate(lista_transacciones):
        if obj_transaccion.id == id_transaccion:
            return obj_transaccion

    raise HTTPException(
        status_code=400,
        detail=f"La transacción con id {id_transaccion} no existe"
    )


# Endpoint para crear una transacción
@rutas_transacciones.post("/transacciones/{factura_id}", response_model=Transaccion)
async def crear_transaccion(factura_id: int, datos_transaccion: TransaccionCrear):

    factura_encontrada = None

    for factura in lista_facturas:
        if factura.id == factura_id:
            factura_encontrada = factura

    if not factura_encontrada:
        raise HTTPException(
            status_code=400,
            detail=f"La factura con id {factura_id} no existe"
        )

    transaccion_val = Transaccion.model_validate(datos_transaccion.model_dump())
    transaccion_val.id = len(lista_transacciones) + 1
    transaccion_val.id_factura = factura_id

    factura_encontrada.transacciones.append(transaccion_val)
    lista_transacciones.append(transaccion_val)

    return transaccion_val


# Endpoint para editar una transacción
@rutas_transacciones.patch("/transacciones/{id_transaccion}", response_model=Transaccion)
async def editar_transaccion(id_transaccion: int, datos_transaccion: TransaccionEditar):

    for i, obj_transaccion in enumerate(lista_transacciones):
        if obj_transaccion.id == id_transaccion:

            transaccion_val = Transaccion.model_validate(datos_transaccion.model_dump())
            transaccion_val.id = id_transaccion
            transaccion_val.id_factura = obj_transaccion.id_factura

            lista_transacciones[i] = transaccion_val

            return transaccion_val

    raise HTTPException(
        status_code=400,
        detail=f"La transacción con id {id_transaccion} no existe"
    )


# Endpoint para eliminar una transacción
@rutas_transacciones.delete("/transacciones/{id_transaccion}", response_model=Transaccion)
async def eliminar_transaccion(id_transaccion: int):

    for i, obj_transaccion in enumerate(lista_transacciones):
        if obj_transaccion.id == id_transaccion:
            transaccion_eliminada = lista_transacciones.pop(i)
            return transaccion_eliminada

    raise HTTPException(
        status_code=400,
        detail=f"La transacción con id {id_transaccion} no existe"
    )