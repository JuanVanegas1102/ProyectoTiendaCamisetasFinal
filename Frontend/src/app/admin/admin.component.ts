import { Component } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { CalendarioService } from '../servicios/calendario.service';
import { Evento } from '../modelos/evento';
import { HttpClient } from '@angular/common/http';
import { estudianteConResponse } from '../modelos/responses';
import { estudianteResponse } from '../modelos/responses';
import { AdminService } from '../admin.service';

@Component({
  selector: 'app-admin',
  templateUrl: './admin.component.html',
  styleUrls: ['./admin.component.css']
})
export class AdminComponent {
  periodo:string = "202301"
  listaPeriodos: Array<string> = []




  constructor(private router:Router,private route:ActivatedRoute,private calenService:CalendarioService,private http:HttpClient,private adminService:AdminService){

  }

  ngOnInit(){
    if(this.router.url != "/Admin"){
      this.router.navigate(['Admin'])
    }
    if(!this.adminService.hayUsuarioLogeado){
      this.router.navigate(['login'])
    }
    this.calenService.actualizarCalendario(this.periodo)
    this.http.get<estudianteResponse>("http://127.0.0.1:8000/obtenerPeriodos").subscribe((res)=>{
      for (let p of res.data){
        this.listaPeriodos.push(p[0])
      }
    })
  }

  abrirCalendario(){
    this.router.navigate(['Calendario',this.periodo],{relativeTo:this.route})
  }

  abrirAsistencia(){
    this.router.navigate(['Asistencia',this.periodo],{relativeTo:this.route})
  }

  cambioPeriodo(){
    this.router.navigate(['Admin'])
    this.calenService.actualizarCalendario(this.periodo)
  }

  habilitarSeleccion(){
    return (this.calenService.estadoPlaneacion() === "Activo" || this.calenService.estadoPlaneacion() === "error" )
  }

  habilitarAsistencia(){
    let ensayoHoy = this.calenService.obtenerEnsayoHoy()
    if(ensayoHoy === undefined){
      return true
    }else return false
  }

  habilitarLiquidacion(){
    return !this.calenService.liquidacionValida()
  }
  

  habilitarCalendario(){
    return this.calenService.calendario.length == 0
  }


}
