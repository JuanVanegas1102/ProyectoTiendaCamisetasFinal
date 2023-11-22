import { Injectable } from '@angular/core';
import { Evento } from '../modelos/evento';
import { HttpClient } from '@angular/common/http';
import { estudianteResponse } from '../modelos/responses';

@Injectable({
  providedIn: 'root'
})
export class CalendarioService {
  calendario: Array<Evento> = []
  eventosAhora: Array<Evento> = []
  constructor(private http: HttpClient) { }

  actualizarCalendario(periodo: string) {
    this.http.get<estudianteResponse>("http://127.0.0.1:8000/calendario/" + periodo).subscribe(
      {
        next: (res) => {
          this.calendario = []
          this.eventosAhora = []
          let ahora = new Date()
          for (let e of res.data) {
            let evento = new Evento()
            evento.nombreObra = e[0]
            evento.tipoEvento = e[1]
            evento.estado = e[2]
            evento.fechaI = this.crearFecha(e[3].toString())
            evento.fechaF = this.crearFecha(e[4].toString())
            evento.consecCalen = e[6]
            evento.idObra = e[5]
            evento.idTipoCalen = e[7] 
            if (evento.fechaI < ahora && evento.fechaF > ahora) {
              this.eventosAhora.push(evento)
            }
            this.calendario.push(evento)
          }
        }
      })
  }

  obtenerEnsayoHoy(){
    for(let e of this.eventosAhora){
      if (e.tipoEvento === "Ensayo"){
        return e
      }
    }
    return undefined
  }

  liquidacionValida(){
    if (this.eventosAhora.length != 0 || this.calendario.length == 0){
      return false
    }else{
      let hoy = new Date()
      for (let e of this.calendario.reverse()){
        if (e.tipoEvento == "Ensayo" || e.tipoEvento == "Funcion"){
          if(e.fechaF > hoy){
            return false
          }
        }
      }
    }
    return true
  }

  estadoPlaneacion() {
    for (let e of this.calendario) {
      if (e.idTipoCalen === "PA") {
        return e.estado
      }
    }
    return "error"
  }



  crearFecha(fechaS: string) {
    let fechaSeparada = fechaS.split("T")
    let diaLista = fechaSeparada[0].split("-")
    let horaLista = fechaSeparada[1].split(":")
    let fecha = new Date(parseInt(diaLista[0]), parseInt(diaLista[1]) - 1, parseInt(diaLista[2]), parseInt(horaLista[0]), parseInt(horaLista[1]))
    return fecha
  }


}
