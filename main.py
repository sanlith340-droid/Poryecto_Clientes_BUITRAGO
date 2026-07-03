from fastapi import FastAPI, HTTPException , status
from modelos.clientes import Cliente, ClienteCrear , ClienteEditar
from modelos.facturas import Factura , FacturaCrear , FacturaEditar
from modelos.transacciones import Transaccion , TransaccionCrear , TransaccionEditar

app = FastAPI()



    
#variables lista de clientes
lista_clientes:list[Cliente] = []
lista_facturas:list[Factura] = []  
lista_transacciones:list[Transaccion] = [] 

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
        raise HTTPException(status_code=400, detail=f"El cliente con id {cliente_id} , no existe")
        
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
            cliente_eliminado = lista_clientes.pop(i)
            return cliente_eliminado
    raise HTTPException(status_code=400, detail=f"El cliente con id {cliente_id} , no existe")

#||||||||||||||||||||||||||||||||||||||||||
#Endpoint  para factura 

@app.get("/facturas", response_model=list[Factura])
async def listar_facturas():
    return lista_facturas


@app.get("/facturas/{factura_id}", response_model=Factura)
async def listar_factura(id_factura: int):
     #recorrer la lista facturas
    for i , obj_factura in enumerate (lista_facturas):
        if obj_factura.id == id_factura:
            return  obj_factura 
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                        detail=f"La factura con id {id_factura} , no existe")

@app.post("/facturas/{cliente_id}", response_model=Factura)
async def crear_factura(cliente_id: int, datos_factura: FacturaCrear):
    
    cliente_encontrado = None
    #Buscar el cliente 
    for cliente in lista_clientes:
        if cliente.id == cliente_id:
            cliente_encontrado = cliente
    #Mensaje si no existe el cliente
    if not cliente_encontrado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"El cliente con id {cliente_id} , no existe")
    
    #validar datos de la factura
    factura_val = Factura.model_validate(datos_factura.model_dump())
    factura_val.cliente = cliente_encontrado
    #generar id de factura
    factura_val.id = len(lista_facturas)+1
    lista_facturas.append(factura_val)
    return factura_val

@app.patch("/facturas/{id_factura}", response_model=Factura)
async def editar_factura(id_factura: int, datos_factura: Factura):
    pass

@app.delete("/facturas/{id_factura}", response_model=Factura)
async def eliminar_factura(id_factura):
    pass

#||||||||||||||||||||||||||||||||||||||||||||||||||
#Crear los endpoints para transacciones

@app.get("/transacciones", response_model=list[Transaccion])
async def listar_ftransacciones():
    return lista_transacciones


@app.get("/transacciones/{id_transaccion}", response_model=Transaccion)
async def listar_transaccion(id_transaccion: int):
    pass


@app.post("/transacciones/{factura_id}", response_model=Transaccion)
async def crear_transaccion(factura_id: int, datos_transaccion: TransaccionCrear):
    #Buscar la factura  
    factura_encontrada = None 
    for factura in lista_facturas:
        if factura.id == factura_id:
            factura_encontrada = factura
    #Mensaje si no existe la factura
    if not factura_encontrada:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"La factura con id {factura_id} , no existe")
    
    #validar datos de la transaccion
    transaccion_val= Transaccion.model_validate(datos_transaccion.model_dump())
    transaccion_val.id_factura = factura_id
    factura_encontrada.transacciones.append(transaccion_val)
    
    #generar id de transaccion
    transaccion_val.id = len(lista_transacciones)+1
    
    return transaccion_val


@app.patch("/transacciones/{id_transaccion}", response_model=Transaccion)
async def editar_transaccion(id_transaccion: int, datos_transaccion: TransaccionEditar):
    for i, obj_transaccion in enumerate(lista_transacciones):
        if obj_transaccion.id == id_transaccion:
            # Validar los datos recibidos
            transaccion_val = Transaccion.model_validate(datos_transaccion.model_dump())
            transaccion_val.id = id_transaccion

            # Reemplazar la transacción en la lista
            lista_transacciones[i] = transaccion_val

            return transaccion_val

    raise HTTPException(
        status_code=400,
        detail=f"La transacción con id {id_transaccion} no existe"
    )


@app.delete("/transacciones/{id_transaccion}", response_model=Transaccion)
async def eliminar_transaccion(id_transaccion: int):
    for i, obj_transaccion in enumerate(lista_transacciones):
        if obj_transaccion.id == id_transaccion:
            transaccion_eliminada = lista_transacciones.pop(i)
            return transaccion_eliminada

    raise HTTPException(
        status_code=400,
        detail=f"La transacción con id {id_transaccion} no existe"
    )