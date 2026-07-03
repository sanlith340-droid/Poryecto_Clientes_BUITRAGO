from pydantic import BaseModel

#crear el modelo transaccion(id,cantidad,vr_unitario,id_factura)
class TransaccionBase(BaseModel):
    cantidad: int
    vr_unitario: float
    

class TransaccionCrear(TransaccionBase):
    pass

class TransaccionEditar(TransaccionBase):
    pass

class Transaccion(TransaccionBase):
    id: int | None = None
    id_factura: int | None = None  #aqui va la relacion con el modelo factura solo un campo
    #aqui va la relacion con el modelo factura solo un campo