from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from BD import ConexionBD
from Correo import CorreoSer

class login(BaseModel):
    correo:str
    contrasena:str

class correo(BaseModel):
    asunto:str
    contenidos:str
    remitente:str

class usuario(BaseModel):
    nombreUsuario:str
    contrasena:str
    correo:str
    nombres:str
    apellidos:str
    telefono:str

class estampa(BaseModel):
    nombre:str
    descripcion:str
    imagen1:str
    imagen2:str
    imagen3:str
    precio:float
    idtematica: str

class categoria(BaseModel):
    categoria: int

app = FastAPI()

origins = [
    "http://localhost:4200"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/listaEstampas')
async def root():
    result = ConexionBD.consultarEstampas()
    return {"data":result}

@app.post('/numCategoria')
async def root(s:categoria):
    result = ConexionBD.consultarCategoria(s.categoria)
    return {"message":"hola mi loco"}

@app.get('/listaTallas')
async def root():
    result = ConexionBD.consultarTallas()
    return {"data":result}

@app.get('/listaTematica')
async def root():
    result = ConexionBD.consultarTematica()
    return {"data":result}

@app.post('/agregarUsuario')
async def root(s:usuario):
    ConexionBD.agregarUsuario(s.nombreUsuario, s.contrasena, s.correo, s.nombres, s.apellidos, s.telefono)
    return {"message":"hola mi loco"}

@app.post('/agregarEstampa')
async def root(s:estampa):
    ConexionBD.agregarEstampa(s.nombre,s.descripcion,s.imagen1,s.imagen2,s.imagen3,s.precio,s.idtematica)
    return {"message":"hola mi loco"}

@app.post('/validate')
async def root(l:login):
    valid = ConexionBD.validarLogin(l.correo,l.contrasena)
    if valid:
        return {"message":"logeado correctamente",
                "codigo" : 202}
    else:
        return {"message":"El Correo o la contraseña son incorrectos, intente nuevamente",
                "codigo" : 404}
        
@app.post('/enviarCorreo')
async def root(s:correo):
    CorreoSer.enviarCorreo(s.asunto,s.contenidos,s.remitente)
    return {"message":"hola mi loco"}

