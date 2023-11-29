import { HttpClient } from '@angular/common/http';
import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { carritoResponse, creditoResponse, totalResponse } from '../modelos/responses';
import { AdminService } from '../admin.service';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-carrito',
  templateUrl: './carrito.component.html',
  styleUrls: ['./carrito.component.css']
})
export class CarritoComponent {
  listaCarrito : Array<any>
  listaTotal : Array<any>
  listaCredito : Array<any>
  mensajeError:string;
  responseCode:number;
  hayError:boolean = false;
  public show:boolean = false;
  public buttonName:any = 'Show';
  formulario!: FormGroup;

  constructor(private http:HttpClient, private router:Router, private adminServicio:AdminService,private fb:FormBuilder)
  {
    
  }

  ngOnInit(){

    if(this.adminServicio.hayUsuarioLogeado){
      this.router.navigate(['/carrito'])
    }else{
      this.router.navigate(['/login'])
    }

    this.http.get<carritoResponse>("http://127.0.0.1:8000/listaCarrito").subscribe(
      {
        next:(res)=>{
          this.listaCarrito = res.data
          console.log(this.listaCarrito)
        },
        error: (error) => {
          console.log(error)
        }
      })

    this.http.get<totalResponse>("http://127.0.0.1:8000/totalCarrito").subscribe(
        {
          next:(res)=>{
            this.listaTotal = res.data
            console.log(this.listaTotal)
          },
          error: (error) => {
            console.log(error)
          }
      })

      this.http.get<creditoResponse>("http://127.0.0.1:8000/creditoUsuario").subscribe(
        {
          next:(res)=>{
            this.listaCredito = res.data
            console.log(this.listaCredito)
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
  
  eliminarProducto(dato){

    const datoEliminar = { 
      datoEliminacion: dato
    }

    this.hayError = false;
    console.log(datoEliminar);
  
    this.http.post("http://127.0.0.1:8000/eliminarProducto",datoEliminar).subscribe(
      {
        next: res => this.mostrarError("Envio exitoso!!!!"),
        error: err => this.mostrarError("Error al enviar la categoria")
      })

      this.http.get<carritoResponse>("http://127.0.0.1:8000/listaCarrito").subscribe(
      {
        next:(res)=>{
          this.listaCarrito = res.data
          console.log(this.listaCarrito)
        },
        error: (error) => {
          console.log(error)
        }
      })

    this.http.get<totalResponse>("http://127.0.0.1:8000/totalCarrito").subscribe(
        {
          next:(res)=>{
            this.listaTotal = res.data
            console.log(this.listaTotal)
          },
          error: (error) => {
            console.log(error)
          }
      })

      this.http.get<creditoResponse>("http://127.0.0.1:8000/creditoUsuario").subscribe(
        {
          next:(res)=>{
            this.listaCredito = res.data
            console.log(this.listaCredito)
          },
          error: (error) => {
            console.log(error)
          }
      })
  }

  toggle() {
    this.show = !this.show;

    // Change the name of the button.
    if(this.show)  
      this.buttonName = "Hide";
    else
      this.buttonName = "Show";
  }

  crearFormulario(){
    this.formulario = this.fb.group({
      numDocumento:['',Validators.required],
      direccionEntrega:['',Validators.required]
    })
  }

  enviarFormulario(){
    
    const datosFormulario = {
      numDocumento:this.formulario.value.numDocumento,
      direccionEntrega:this.formulario.value.direccionEntrega
    }

    this.hayError = false
    console.log(datosFormulario)
    this.http.post("http://127.0.0.1:8000/agregarDatosFactura",datosFormulario).subscribe(
      {
        next: res => this.mostrarError("Envio exitoso!!!!"),
        error: err => this.mostrarError("Error al enviar el formulario")
      })
  }

}
