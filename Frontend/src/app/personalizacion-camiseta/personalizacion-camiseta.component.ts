import { Component } from '@angular/core';
import { estampaSeleccionadaResponse, modeloCamisetaResponse, stockResponse, tallaResponse } from '../modelos/responses';
import { HttpClient } from '@angular/common/http';
import { AdminService } from '../admin.service';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';

@Component({
  selector: 'app-personalizacion-camiseta',
  templateUrl: './personalizacion-camiseta.component.html',
  styleUrls: ['./personalizacion-camiseta.component.css']
})
export class PersonalizacionCamisetaComponent {

  listaEstampas : Array<any>
  listaStock : Array<any>
  formulario!: FormGroup;
  mensajeError:string;
  responseCode:number;
  hayError:boolean = false;
  listaTallas : Array<any>
  listaModeloCamiseta : Array<any>

  constructor(private http : HttpClient,private  fb:FormBuilder, private router:Router, private adminServicio:AdminService)
  {
    
  }
  ngOnInit(){

    if(this.adminServicio.hayUsuarioLogeado){
      this.router.navigate(['/personalizacion-camiseta'])
    }else{
      this.router.navigate(['/login'])
    }


    this.http.get<estampaSeleccionadaResponse>("http://127.0.0.1:8000/listaEstampaSeleccionada").subscribe(
      {
        next:(res)=>{
          this.listaEstampas = res.data
          console.log(this.listaEstampas)
        },
        error: (error) => {
          console.log(error)
        }
      })

      this.http.get<tallaResponse>("http://127.0.0.1:8000/listaTallas").subscribe(
      {
        next:(res)=>{
          this.listaTallas = res.data
          console.log(this.listaTallas)
        },
        error: (error) => {
          console.log(error)
        }
      })

      this.http.get<modeloCamisetaResponse>("http://127.0.0.1:8000/listaModeloCamiseta").subscribe(
      {
        next:(res)=>{
          this.listaModeloCamiseta = res.data
          console.log(this.listaModeloCamiseta)
        },
        error: (error) => {
          console.log(error)
        }
      })
      this.crearFormulario()
  }

  mostrarError(mensaje:string){
    this.hayError = true
    this.mensajeError = mensaje
  }

  cambiarMaximaCantidad(value:any){

    const datoTipoCamiseta = { 
      seleccionTipoCamiseta: value.target.value
    }

    this.hayError = false;
    console.log(datoTipoCamiseta);
  
    this.http.post("http://127.0.0.1:8000/seleccionTipoCamiseta",datoTipoCamiseta).subscribe(
      {
        next: res => this.mostrarError("Envio exitoso!!!!"),
        error: err => this.mostrarError("Error al enviar la categoria")
      })

      this.http.get<stockResponse>("http://127.0.0.1:8000/cantidadStock").subscribe(
      {
        next:(res)=>{
          this.listaStock  = res.data
          console.log(this.listaStock )
        },
        error: (error) => {
          console.log(error)
        }
      })
  }

  agregarCarrito(){
    
    const datosFormulario = {
      idmodelocamiseta:this.formulario.value.idmodelocamiseta,
      idtalla:this.formulario.value.idtalla,
      cantidad:this.formulario.value.cantidad,
      colorCamiseta:this.formulario.value.colorCamiseta
    }

    this.hayError = false
    console.log(datosFormulario)

    this.http.post("http://127.0.0.1:8000/agregarCarrito",datosFormulario).subscribe(
      {
        next: res=> this.mostrarError("Envio exitoso!!!!"),
        error: err => this.mostrarError("Error al enviar el formulario")
      })
  }

  crearFormulario(){
    this.formulario = this.fb.group({
      idmodelocamiseta:['',Validators.required],
      idtalla:['',Validators.required],
      cantidad:['',Validators.required],
      colorCamiseta:['',Validators.required]
    })
  }
}
