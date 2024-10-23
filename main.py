from fastapi import FastAPI
from app.database.configuration import engine
from app.api.models.tablasSQL import Base
from app.api.routes.endpoints import rutas

from starlette.responses import RedirectResponse

# crear las tablas de sql desde python
Base.metadata.create_all(bind=engine)

# Variable para administrar la applicacion

app=FastAPI()

# Activar el api
@app.get("/")
def main():
    return RedirectResponse(url="/docs")

app.include_router(rutas)