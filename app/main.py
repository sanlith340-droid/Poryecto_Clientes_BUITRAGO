from fastapi import FastAPI, HTTPException, status
from .modelos.clientes import Cliente, Clientecrear, ClienteEditar
from .modelos.facturas import Factura, FacturaCrear, FacturaEditar
from .modelos.transacciones import Transaccion,TransaccionCrear, TransaccionEditar
from .enrutadores import clientes, factura, transacciones
from .enrutadores.clientes import rutas_clientes
from .enrutadores.factura import rutas_facturas
from .enrutadores.transacciones import rutas_transacciones
from .listas import lista_clientes, lista_facturas, lista_transacciones
from .conexion_bd import crear_tablas

app = FastAPI(lifespan=crear_tablas)


#incluir rutas de clientes
app.include_router(clientes.rutas_clientes, tags=["Clientes"])
app.include_router(factura.rutas_facturas, tags=["Facturas"])
app.include_router(transacciones.rutas_transacciones, tags=["Transacciones"])





