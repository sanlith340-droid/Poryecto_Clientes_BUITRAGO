from fastapi import APIRouter, HTTPException, status
from app.modelos.facturas import Factura, FacturaCrear, FacturaEditar
from app.enrutadores.clientes import lista_clientes

rutas_facturas = APIRouter()
lista_facturas: list[Factura] = []


# Endpoint para listar todas las facturas
@rutas_facturas.get("/facturas", response_model=list[Factura])
async def listar_facturas():
    return lista_facturas


# Endpoint para listar una factura
@rutas_facturas.get("/facturas/{factura_id}", response_model=Factura)
async def listar_factura(factura_id: int):

    for i, obj_factura in enumerate(lista_facturas):
        if obj_factura.id == factura_id:
            return obj_factura

    raise HTTPException(
        status_code=400,
        detail=f"La factura con id {factura_id} no existe"
    )


# Endpoint para crear una factura
@rutas_facturas.post("/facturas/{cliente_id}", response_model=Factura)
async def crear_factura(cliente_id: int, datos_factura: FacturaCrear):

    cliente_encontrado = None

    for cliente in lista_clientes:
        if cliente.id == cliente_id:
            cliente_encontrado = cliente

    if not cliente_encontrado:
        raise HTTPException(
            status_code=400,
            detail=f"El cliente con id {cliente_id} no existe"
        )

    factura_val = Factura.model_validate(datos_factura.model_dump())
    factura_val.id = len(lista_facturas) + 1
    factura_val.cliente = cliente_encontrado

    lista_facturas.append(factura_val)

    return factura_val


# Endpoint para editar una factura
@rutas_facturas.patch("/facturas/{factura_id}", response_model=Factura)
async def editar_factura(factura_id: int, datos_factura: FacturaEditar):

    for i, obj_factura in enumerate(lista_facturas):
        if obj_factura.id == factura_id:

            factura_val = Factura.model_validate(datos_factura.model_dump())
            factura_val.id = factura_id
            factura_val.cliente = obj_factura.cliente

            lista_facturas[i] = factura_val

            return factura_val

    raise HTTPException(
        status_code=400,
        detail=f"La factura con id {factura_id} no existe"
    )


# Endpoint para eliminar una factura
@rutas_facturas.delete("/facturas/{factura_id}", response_model=Factura)
async def eliminar_factura(factura_id: int):

    for i, obj_factura in enumerate(lista_facturas):
        if obj_factura.id == factura_id:
            factura_eliminada = lista_facturas.pop(i)
            return factura_eliminada

    raise HTTPException(
        status_code=400,
        detail=f"La factura con id {factura_id} no existe"
    )