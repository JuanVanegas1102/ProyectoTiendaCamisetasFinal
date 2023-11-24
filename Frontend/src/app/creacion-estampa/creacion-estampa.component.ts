import { HttpClient, HttpResponse } from '@angular/common/http';
import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { LogResponse } from '../modelos/responses';
import { Router } from '@angular/router';
import { interval } from 'rxjs';
import { AdminService } from '../admin.service';

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
  
  constructor(private http : HttpClient,private  fb:FormBuilder, private router:Router, private adminServicio:AdminService){

  }

  ngOnInit(){
    if(this.adminServicio.hayUsuarioLogeado){
      this.router.navigate(['/creacionEstampa'])
    }else{
      this.router.navigate(['/login'])
    }

    //this.crearFormulario();
  }

}