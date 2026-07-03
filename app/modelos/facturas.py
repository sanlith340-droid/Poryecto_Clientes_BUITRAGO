from pydantic import BaseModel, computed_field
from sqlmodel import SQLModel, Field, Relationship
from .transacciones import Transaccion
from .clientes import Cliente, ClienteLeer
from datetime import datetime

#Crear el modelo de transacciones (id,fecha, vr_total, cliente )
#properity// sirve para convertir un metodo de una clase en una propiedad de lectura
#computed_field // sirve para que pydantic reconozca la propiedad como un campo de lectura


class FacturaBase(SQLModel):
    fecha: str = Field(default=datetime.now()) 
    #cliente: Cliente
    #transacciones: list[Transaccion] = []


    @computed_field
    @property
    def vr_total(self) -> float:        
        total_facturas = 0.0
        if self.transacciones== None:
            return total_facturas
        #recorrer las transacciones, segun el id de la factura

        for transaccion in self.transacciones:
            total_facturas += transaccion.vr_unitario * transaccion.cantidad

        return total_facturas

class FacturaCrear(FacturaBase):
    
    cliente: Cliente
    transacciones: list[Transaccion] =[]


class FacturaEditar(FacturaBase):
    pass

class Factura(FacturaBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    cliente_id: int = Field(default=None, foreign_key="cliente.id")
    #crear relaciones virtuales,transacciones - NO en la bd
    transacciones: list[Transaccion] = Relationship(back_populates="factura")
    cliente: Cliente = Relationship(back_populates="facturas")

#modelo para mostrar al usurario o el cliente
class FacturaLeer(FacturaBase):
    id: int
    cliente: ClienteLeer

class FacturaLeerCompuesta(FacturaLeer):
    transacciones: list[Transaccion] = []
    