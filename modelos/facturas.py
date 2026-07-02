from pydantic import BaseModel

from modelos.clientes import Cliente

#Crear el modelo de transacciones (id,fecha, vr_total, cliente )

class FacturaBase(BaseModel):
    fecha: str
    vr_total: float #calcular (cantidad * vr_unitario)
    cliente : Cliente  # Esta es la relacion con el cliente (objeto)
    
class FacturaCrear(FacturaBase):
    pass

class Factura(FacturaBase):
    id: int | None = None