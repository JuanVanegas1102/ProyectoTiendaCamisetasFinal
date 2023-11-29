from fastapi import FastAPI
from fastapi.middleware import Middleware
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

class detallefactura(BaseModel):
    idmodelocamiseta: str
    idtalla : str
    cantidad: int
    colorCamiseta: str
    
class datosfactura(BaseModel):
    numDocumento: str
    direccionEntrega : str

class categoria(BaseModel):
    categoria: int

class seleccionTipoCamiseta(BaseModel):
    seleccionTipoCamiseta: str

class seleccion(BaseModel):
    seleccion: str
    
class eliminar(BaseModel):
    datoEliminacion: str

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

@app.get("/")
async def main():
   return {"message": "Hello World"}

@app.get('/listaEstampas')
async def root():
    result = ConexionBD.consultarEstampas()
    return {"data":result}

@app.get('/listaCarrito')
async def root():
    result = ConexionBD.consultarCarrito()
    return {"data":result}

@app.get('/totalCarrito')
async def root():
    result = ConexionBD.totalCarrito()
    return {"data":result}

@app.get('/creditoUsuario')
async def root():
    result = ConexionBD.consultarCredito()
    return {"data":result}

@app.post('/eliminarProducto')
async def root(s:eliminar):
    result = ConexionBD.eliminarProducto(s.datoEliminacion)
    return {"message":"hola mi loco"}

@app.post('/numCategoria')
async def root(s:categoria):
    result = ConexionBD.consultarCategoria(s.categoria)
    return {"message":"hola mi loco"}

@app.post('/seleccionTipoCamiseta')
async def root(s:seleccionTipoCamiseta):
    result = ConexionBD.seleccionTipo(s.seleccionTipoCamiseta)
    return {"message":"hola mi loco"}

@app.get('/cantidadStock')
async def root():
    result = ConexionBD.consultarStock()
    return {"data":result}

@app.post('/estampaSeleccionada')
async def root(s:seleccion):
    result = ConexionBD.estampaSeleccionada(s.seleccion)
    return {"message":"hola mi loco"}

@app.get('/listaEstampaSeleccionada')
async def root():
    result = ConexionBD.consultarEstampaSeleccionada()
    return {"data":result}

@app.get('/listaTallas')
async def root():
    result = ConexionBD.consultarTallas()
    return {"data":result}

@app.get('/listaTematica')
async def root():
    result = ConexionBD.consultarTematica()
    return {"data":result}

@app.get('/listaModeloCamiseta')
async def root():
    result = ConexionBD.consultarModeloCamiseta()
    return {"data":result}

@app.post('/agregarUsuario')
async def root(s:usuario):
    ConexionBD.agregarUsuario(s.nombreUsuario, s.contrasena, s.correo, s.nombres, s.apellidos, s.telefono)
    return {"message":"hola mi loco"}

@app.post('/agregarEstampa')
async def root(s:estampa):
    ConexionBD.agregarEstampa(s.nombre,s.descripcion,s.imagen1,s.imagen2,s.imagen3,s.precio,s.idtematica)
    return {"message":"hola mi loco"}

@app.post('/agregarCarrito')
async def root(s:detallefactura):
    ConexionBD.agregarCarrito(s.idmodelocamiseta,s.idtalla,s.cantidad,s.colorCamiseta)
    return {"message":"hola mi loco"}

@app.post('/agregarDatosFactura')
async def root(s:datosfactura):
    ConexionBD.agregarDatosFactura(s.numDocumento,s.direccionEntrega)
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

