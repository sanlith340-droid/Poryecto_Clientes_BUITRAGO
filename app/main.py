from fastapi import FastAPI, HTTPException , status
from app.enrutadores.clientes import rutas_clientes
from app.enrutadores.factura import rutas_factura
from app.enrutadores.transacciones import rutas_transacciones
from app.conexion_bd import crear_tablas

app = FastAPI(lifespan=crear_tablas) 



#Incluir ruta de clientes
app.include_router(rutas_clientes, tags=["Clientes"])
#Incluir ruta de facturas
app.include_router(rutas_factura, tags=["Facturas"])
#Incluir ruta de transacciones
app.include_router(rutas_transacciones, tags=["Transacciones"])

#x=12 - init <- creacion de variable y su tipo de dato
#x=ana - str

#get: obtener o listar





