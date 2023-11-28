import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { InicioPaginaComponent } from './inicio-pagina/inicio-pagina.component';
import { AppComponent } from './app.component';
import { AdminComponent } from './admin/admin.component';
import { LoginComponent } from './login/login.component';
import { RegistroComponent } from './registro/registro.component';
import { CreacionEstampaComponent } from './creacion-estampa/creacion-estampa.component';
import { PersonalizacionCamisetaComponent } from './personalizacion-camiseta/personalizacion-camiseta.component';

const routes: Routes = [
  {path:'',component:InicioPaginaComponent},
  {path:'login', component:LoginComponent},
  {path:'registro', component:RegistroComponent},
  {path:'creacionEstampa', component:CreacionEstampaComponent},
  {path:'personalizacionCamiseta', component:PersonalizacionCamisetaComponent},
  {
    path:'Admin', component:AdminComponent,
    children:[
      
    ]
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
  bootstrap: [AppComponent]
})
export class AppRoutingModule { }
