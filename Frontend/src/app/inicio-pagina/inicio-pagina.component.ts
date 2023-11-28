import { HttpClient } from '@angular/common/http';
import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { estampaResponse } from '../modelos/responses'; 
import {CargarScriptsService} from "./../servicios/cargar-scripts.service";

@Component({
  selector: 'app-inicio',
  templateUrl: './inicio-pagina.component.html',
  styleUrls: ['./inicio-pagina.component.css','../css/bootstrap.css','../css/fontawesome-all.css','../css/login_overlay.css','../css/owl.carousel.css','../css/owl.theme.css',
              '../css/shop.css','../css/style.css','../css/style6.css']
})
export class InicioPaginaComponent {
  images = ["logo.png","s1.jpg","s2.jpg","s3.jpg","s4.jpg","m1.jpg","m2.jpg","m3.jpg","m4.jpg","s5.jpg","s6.jpg","s7.jpg","s8.jpg","s9.jpg","s10.jpg","banner4.jpg","banner3.jpg"].map((n) => `assets/images/${n}`);
  listaEstampas : Array<any>
  mensajeError:string;
  responseCode:number;
  hayError:boolean = false;
  constructor(private _CargaScripts:CargarScriptsService, private http:HttpClient, private router:Router)
  {
    _CargaScripts.Carga(["jquery-2.2.3.min","jquery-ui","jquery.easing.min","jquery.flexslider","jquery.magnific-popup","bootstrap","modernizr-2.6.2.min","classie-search","creditly","demo1-search","easing","easy-responsive-tabs","imagezoom","minicart","move-top","owl.carousel","simplyCountdown"])
  }

  ngOnInit(){

    this.http.get<estampaResponse>("http://127.0.0.1:8000/listaEstampas").subscribe(
      {
        next:(res)=>{
          this.listaEstampas = res.data
          console.log(this.listaEstampas)
        },
        error: (error) => {
          console.log(error)
        }
      })
    
  }

  mostrarError(mensaje:string){
    this.hayError = true
    this.mensajeError = mensaje
  }

  async mandarCategoria(code:number,message:string){
    this.responseCode = code
    this.mensajeError = message
    if(this.responseCode ==404){
      this.hayError = true
    }else{
    }
  }

  cambiarCatalogo(value:any){

    const datoCategoria = { 
      categoria: value.target.value
    }

    this.hayError = false;
    console.log(datoCategoria);
  
    this.http.post("http://127.0.0.1:8000/numCategoria",datoCategoria).subscribe(
      {
        next: res => this.mostrarError("Envio exitoso!!!!"),
        error: err => this.mostrarError("Error al enviar la categoria")
      })

      this.http.get<estampaResponse>("http://127.0.0.1:8000/listaEstampas").subscribe(
      {
        next:(res)=>{
          this.listaEstampas = res.data
          console.log(this.listaEstampas)
        },
        error: (error) => {
          console.log(error)
        }
      })
  }

  guardarSeleccion(dato){
    const datoSeleccion = { 
      seleccion: dato
    }

    this.hayError = false;
    console.log(datoSeleccion);
  
    this.http.post("http://127.0.0.1:8000/estampaSeleccionada",datoSeleccion).subscribe(
      {
        next: res =>{
          this.mostrarError("Envio exitoso!!!!"),
          this.router.navigate(['/personalizacionCamiseta'])
        },
        error: err => this.mostrarError("Error al enviar la estampa seleccionada")
      })
  }


}