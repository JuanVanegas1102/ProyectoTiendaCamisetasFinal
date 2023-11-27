import { HttpClient, HttpResponse } from '@angular/common/http';
import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { LogResponse, tematicaResponse } from '../modelos/responses';
import { Router } from '@angular/router';
import { interval } from 'rxjs';
import { AdminService } from '../admin.service';
import { unidadesResponse } from '../modelos/responses';


@Component({
  selector: 'app-creacion-estampa',
  templateUrl: './creacion-estampa.component.html',
  styleUrls: ['./creacion-estampa.component.css']
})

export class CreacionEstampaComponent {
  formulario: FormGroup;
  hayError:boolean = false;
  mensajeError:string;
  responseCode:number;
  bocetos:Map<string,Map<string,string>>;
  listaTematica : Array<any>
  
  constructor(private http : HttpClient,private  fb:FormBuilder, private router:Router, private adminServicio:AdminService){

  }

  ngOnInit(){
    if(this.adminServicio.hayUsuarioLogeado){
      this.router.navigate(['/creacionEstampa'])
    }else{
      this.router.navigate(['/login'])
    }

    this.http.get<tematicaResponse>("http://127.0.0.1:8000/listaTematica").subscribe(
      {
        next:(res)=>{
          this.listaTematica = res.data
          console.log(this.listaTematica)
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

  registrarEstampa(){
    
    const datosFormulario = {
      nombre:this.formulario.value.nombre,
      descripcion:this.formulario.value.descripcion,
      imagen1:this.formulario.value.imagen1,
      imagen2:this.formulario.value.imagen2,
      imagen3:this.formulario.value.imagen3,
      precio:this.formulario.value.precio,
      idtematica:this.formulario.value.idtematica
    }

    this.hayError = false
    console.log(datosFormulario)
    this.http.post("http://127.0.0.1:8000/agregarEstampa",datosFormulario).subscribe(
      {
        next: res => this.mostrarError("Envio exitoso!!!!"),
        error: err => this.mostrarError("Error al enviar el formulario")
      })
  }

  crearFormulario(){
    this.formulario = this.fb.group({
      nombre:['',Validators.required],
      descripcion:['',Validators.required],
      imagen1:['',Validators.required],
      imagen2:['',Validators.required],
      imagen3:['',Validators.required],
      precio:['',Validators.required],
      idtematica:['',Validators.required]
    })
  }
}