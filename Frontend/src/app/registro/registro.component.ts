import { HttpClient } from '@angular/common/http';
import { Component } from '@angular/core';
import { FormBuilder, FormControl, FormGroup,Validators  } from '@angular/forms';
import { Router } from '@angular/router';
import { unidadesResponse } from '../modelos/responses';

@Component({
  selector: 'app-registro',
  templateUrl: './registro.component.html',
  styleUrls: ['./registro.component.css']
})
export class RegistroComponent {

  formulario!: FormGroup;
  hayError:boolean = false;
  mensajeError:string;

  constructor(private fb:FormBuilder,private router:Router, private http:HttpClient){}

  ngOnInit(){

    this.crearFormulario()

  }

  mostrarError(mensaje:string){
    this.hayError = true
    this.mensajeError = mensaje
  }

  enviarFormulario(){
    
    const datosFormulario = {
      nombreUsuario:this.formulario.value.nombreUsuario,
      contrasena:this.formulario.value.contrasena,
      correo:this.formulario.value.correo,
      nombres:this.formulario.value.nombres,
      apellidos:this.formulario.value.apellidos,
      telefono:this.formulario.value.telofono
    }

    this.hayError = false
    console.log(datosFormulario)
    this.http.post("http://127.0.0.1:8000/agregarUsuario",datosFormulario).subscribe(
      {
        next: res => this.mostrarError("Envio exitoso!!!!"),
        error: err => this.mostrarError("Error al enviar el formulario")
      })
  }

  /**
   * this.http.post("http://127.0.0.1:8000/validate",this.formulario.value).subscribe(
      {
        next: res => this.completarLogIn(res.codigo,res.message),
        error: err => this.completarLogIn(404,"Hubo un Error con el servidor, Intentalo nuevamente")
      })
   */

  crearFormulario(){
    this.formulario = this.fb.group({
      nombreUsuario:['',Validators.required],
      correo:['',Validators.compose([Validators.required,Validators.email])],
      contrasena:['',Validators.required],
      nombres:['',Validators.required],
      apellidos:['',Validators.required],
      telofono:['',Validators.required]
    })
  }
}
