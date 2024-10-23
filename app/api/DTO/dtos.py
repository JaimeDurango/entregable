from pydantic import BaseModel,Field
from datetime import date

#LOS DTO SON CLASES QUE ESTABLECEN
#EL MODELO DE TRANSFERENCIA DE DATOS
class UsuarioDTOPeticion(BaseModel):
    nombres:str
    fechaNacimiento:date
    ubicacion:str
    metaAhorro:float
    class Config:
        orm_mode=True

class UsuarioDTORespuesta(BaseModel):
    id:int
    nombres:str
    metaAhorro:float
    class Config:
        orm_mode=True



class GastoDTOPenticion(BaseModel):
    descripcion:str
    categoria:str
    valor:float
    fecha:date
    class Config:
        orm_mode=True
        
class GastoDTORespuesta(BaseModel):
    id:int
    descripcion:str
    categoria:str
    valor:float
    class Config:
        orm_mode=True


class CategoriaDTOPenticion(BaseModel):
    nombre:str
    descripcion:str 
    valor:float
    fecha:date
    class Config:
        orm_mode=True

class CategoriaDTORespuesta(BaseModel):
    id:int
    nombre:str
    valor:float
    fecha:date
    class Config:
        orm_mode=True

class IngresoDTOPeticion(BaseModel):
    id:int
    descripcion:str
    valor:float
    fecha:date
    class Config:
        orm_mode=True
        
class IngresoDTORespuesta(BaseModel):
    id:int
    descripcion:str
    valor:float
    fecha:date
    class Config:
        orm_mode=True