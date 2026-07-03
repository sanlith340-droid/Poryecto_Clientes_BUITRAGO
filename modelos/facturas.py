from pydantic import BaseModel, computed_field

from .transacciones import Transaccion
from .clientes import Cliente 
from datetime import datetime

#Crear el modelo de transacciones (id,fecha, vr_total, cliente )
#properity// sirve para convertir un metodo de una clase en una propiedad de lectura
#computed_field // sirve para que pydantic reconozca la propiedad como un campo de lectura


class FacturaBase(BaseModel):
    fecha: str = datetime.now()
    cliente : Cliente  # Esta es la relacion con el cliente (objeto)
    transacciones: list[Transaccion] = [] 
    
    @computed_field
    @property 
    def vr_total(self) -> float:
        #calcular (cantidad * vr_unitario)
        return 222
    
class FacturaCrear(FacturaBase):
    pass

class FacturaEditar(FacturaBase):
    pass

class Factura(FacturaBase):
    id: int | None = None