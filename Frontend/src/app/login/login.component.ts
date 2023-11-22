import { HttpClient, HttpResponse } from '@angular/common/http';
import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { LogResponse } from '../modelos/responses';
import { Router } from '@angular/router';
import { interval } from 'rxjs';
import { AdminService } from '../admin.service';
import {CargarScriptsService} from "./../servicios/cargar-scripts.service";


@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})

export class LoginComponent {
  formulario: FormGroup;
  hayError:boolean = false;
  mensajeError:string;
  responseCode:number;
  bocetos:Map<string,Map<string,string>>;
  
  constructor(private http : HttpClient,private  fb:FormBuilder, private router:Router, private adminServicio:AdminService){

  }

  ngOnInit(){
    if(this.adminServicio.hayUsuarioLogeado){
      this.router.navigate(['/'])
    }
    this.crearFormulario();
  }

  revisarLogIn(){
    this.hayError = false;
    this.http.post<LogResponse>("http://127.0.0.1:8000/validate",this.formulario.value).subscribe(
      {
        next: res => this.completarLogIn(res.codigo,res.message),
        error: err => this.completarLogIn(404,"Hubo un Error con el servidor, Intentalo nuevamente")
      })
  }

  async completarLogIn(code:number,message:string){
    this.responseCode = code
    this.mensajeError = message
    if(this.responseCode ==404){
      this.hayError = true
    }else{
      this.adminServicio.logearUsuario()
      this.router.navigate(['/'])
      
    }
  }



  crearFormulario(){
    this.formulario = this.fb.group({
      correo:['', Validators.compose([Validators.required,Validators.email])],
      contrasena:['',Validators.required]
    })
  }

}
function next(value: LogResponse): void {
  throw new Error('Function not implemented.');
}

  
  