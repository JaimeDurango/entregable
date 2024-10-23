from sqlalchemy import Column, Integer, String,Float, Date, ForeignKey

from sqlalchemy.orm import relationship

from sqlalchemy.ext.declarative import declarative_base

# llamado ala base para crear tablas
Base = declarative_base()

# DEFINICION DE LAS TABLAS DE MI MODELO

# usuario
class Usuario(Base):
    __tablename__='usuarios'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombres=Column(String(50))
    fechaNacimiento=Column(Date)
    ubicacion=Column(String(100))
    metaAhorro=Column(Float)

class Gasto(Base):
    __tablename__='gastos'
    id =Column(Integer, primary_key=True, autoincrement=True)
    descripcion =Column(String(200))
    categoria =Column(String(50))
    valor =Column(Float)
    fecha =Column(Date)
    id_usuario = Column(Integer, ForeignKey('usuarios.id'))

class Categoria(Base):
    __tablename__='categorias'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50))
    descripcion = Column(String(200))
    valor =Column(Float)
    fecha =Column(Date)

class Ingreso(Base):
    __tablename__='ingresos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    descripcion = Column(String(50))
    valor = Column(Float)
    fecha = Column(Date)