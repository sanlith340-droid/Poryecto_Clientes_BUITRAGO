from fastapi import FastAPI, HTTPException , status
from app.modelos.clientes import Cliente, ClienteCrear, ClienteEditar
from app.modelos.facturas import Factura, FacturaCrear, FacturaEditar
from app.modelos.transacciones import Transaccion, TransaccionCrear, TransaccionEditar
from app.modelos.transacciones import Transaccion, TransaccionCrear, TransaccionEditar

from app.enrutadores import clientes
from app.enrutadores import factura
from app.enrutadores import transacciones

app = FastAPI()

#variables lista de clientes
lista_clientes:list[Cliente] = []
lista_facturas:list[Factura] = []  
lista_transacciones:list[Transaccion] = [] 

#Incluir ruta de clientes
app.include_router(clientes.rutas_clientes, tags=["Clientes"])
#Incluir ruta de facturas
app.include_router(factura.rutas_facturas, tags=["Facturas"])
#Incluir ruta de transacciones
app.include_router(transacciones.rutas_transacciones, tags=["Transacciones"])

#x=12 - init <- creacion de variable y su tipo de dato
#x=ana - str

#get: obtener o listar





