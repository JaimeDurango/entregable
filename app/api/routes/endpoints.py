from fastapi import APIRouter, HTTPException #Libreria para losservicios en la base de datos (Actualizar,Guardar, etc)
from sqlalchemy.orm import Session #comunicacion en la base de datos
from typing import List
from fastapi.params import Depends #Utilizar dependencias del api para comunicacion interna
from app.api.DTO.dtos import UsuarioDTOPeticion, UsuarioDTORespuesta
from app.api.models.tablasSQL import Usuario
from app.api.DTO.dtos import GastoDTOPenticion, GastoDTORespuesta
from app.api.models.tablasSQL import Gasto
from app.api.DTO.dtos import CategoriaDTOPenticion, CategoriaDTORespuesta
from app.api.models.tablasSQL import Categoria
from app.api.DTO.dtos import IngresoDTOPeticion, IngresoDTORespuesta
from app.api.models.tablasSQL import Ingreso
from app.database.configuration import SessionLocal, engine

rutas=APIRouter()

def conectarConBD():
    try:
        baseDatos=SessionLocal()
        yield baseDatos #Activar la base de datos
    except Exception as error:
        baseDatos.rollback()
        raise error
    finally:
        baseDatos.close()

# CONSTRUYENDO NUESTRO SERVICIOS

#Cada servicio (operacion o transaccion en DB) debe programarse como una funcion
#Usuarios
@rutas.post("/usuarios", response_model=UsuarioDTORespuesta, summary="Registrar un usuario en la base de datos")
def guardarUsuario(datosUsuario: UsuarioDTOPeticion, database: Session = Depends(conectarConBD)):
    try:
        usuario = Usuario(
            nombres=datosUsuario.nombres,
            fechaNacimiento=datosUsuario.fechaNacimiento,
            ubicacion=datosUsuario.ubicacion,
            metaAhorro=datosUsuario.metaAhorro
        )
        database.add(usuario)
        database.commit()
        database.refresh(usuario)
        return usuario
    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=400, detail=f"Tenemos un error {error}")

@rutas.get("/usuarios", response_model=List[UsuarioDTORespuesta], summary="Buscar todos los usuarios en base de datos")
def buscarUsuarios(database: Session = Depends(conectarConBD)):
    try:
        usuarios = database.query(Usuario).all()
        return usuarios
    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=400, detail=f"No se puede buscar a los usuarios {error}")
    
# Gasto
    
@rutas.post("/gastos", response_model=GastoDTORespuesta, summary="Registrar un gasto en la base de datos")
def guardarGasto(datosGasto:GastoDTOPenticion, database:Session=Depends(conectarConBD)):
    try:
        gasto=Gasto(
            descripcion=datosGasto.descripcion,
            categoria=datosGasto.categoria,
            valor=datosGasto.valor,
            fecha=datosGasto.fecha
        )
        #Ordenandole a base datos
        database.add(gasto)
        database.commit()
        database.refresh(gasto)
        return gasto

    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=400, detail=f"Tenemos un error {error}")
    
@rutas.get("/gastos", response_model=List[GastoDTORespuesta], summary="Buscar todos los gastos en base de datos")
def buscarGasto(database:Session=Depends(conectarConBD)):
    try:
        gastos=database.query(Gasto).all()
        return gastos

    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=400, detail=f"No se puede buscar a los gastos {error}")
    
    # Categoria
    
@rutas.post("/categorias", response_model=CategoriaDTORespuesta, summary="Registrar un Categoria en la base de datos")
def guardarCategoria(datosCategoria:CategoriaDTOPenticion, database:Session=Depends(conectarConBD)):
    try:
        categoria=Categoria(
            nombre=datosCategoria.nombre,
            descripcion=datosCategoria.descripcion,
            valor=datosCategoria.valor,
            fecha=datosCategoria.fecha
        )
        #Ordenandole a base datos
        database.add(categoria)
        database.commit()
        database.refresh(categoria)
        return categoria

    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=400, detail=f"Tenemos un error {error}")
    
@rutas.get("/categorias", response_model=List[CategoriaDTORespuesta], summary="Buscar todas las Categorias en base de datos")
def buscarCategoria(database:Session=Depends(conectarConBD)):
    try:
        categorias=database.query(Categoria).all()
        return categorias

    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=400, detail=f"No se puede buscar a las categorias {error}")
    
# Ingreso

@rutas.post("/ingresos", response_model=IngresoDTORespuesta, summary="Registrar un Ingreso en la base de datos")
def guardarIngreso(datosIngreso:IngresoDTOPeticion, database:Session=Depends(conectarConBD)):
    try:
        ingreso=Ingreso(
            id=datosIngreso.id,
            descripcion=datosIngreso.descripcion,
            valor=datosIngreso.valor,
            fecha=datosIngreso.fecha
        )
        #Ordenandole a base datos
        database.add(ingreso)
        database.commit()
        database.refresh(ingreso)
        return ingreso

    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=400, detail=f"Tenemos un error {error}")
    
@rutas.get("/ingresos", response_model=List[IngresoDTORespuesta], summary="Buscar todos las Ingreso en base de datos")
def buscarIngreso(database:Session=Depends(conectarConBD)):
    try:
        ingresos=database.query(Ingreso).all()
        return ingresos

    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=400, detail=f"No se puede buscar a los ingresos {error}")

    