import { Component } from '@angular/core';
import { estampaSeleccionadaResponse, modeloCamisetaResponse, tallaResponse } from '../modelos/responses';
import { HttpClient } from '@angular/common/http';
import { AdminService } from '../admin.service';
import { FormBuilder } from '@angular/forms';
import { Router } from '@angular/router';

@Component({
  selector: 'app-personalizacion-camiseta',
  templateUrl: './personalizacion-camiseta.component.html',
  styleUrls: ['./personalizacion-camiseta.component.css']
})
export class PersonalizacionCamisetaComponent {

  listaEstampas : Array<any>
  mensajeError:string;
  responseCode:number;
  hayError:boolean = false;
  listaTallas : Array<any>
  listaModeloCamiseta : Array<any>

  constructor(private http : HttpClient,private  fb:FormBuilder, private router:Router, private adminServicio:AdminService)
  {
    
  }
  ngOnInit(){
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
  }
  
}
