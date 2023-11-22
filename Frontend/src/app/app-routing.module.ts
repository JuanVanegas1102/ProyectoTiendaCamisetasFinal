import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { InicioPaginaComponent } from './inicio-pagina/inicio-pagina.component';
import { AppComponent } from './app.component';
import { AdminComponent } from './admin/admin.component';
import { LoginComponent } from './login/login.component';
import { RegistroComponent } from './registro/registro.component';

const routes: Routes = [
  {path:'',component:InicioPaginaComponent},
  {path:'login', component:LoginComponent},
  {path:'registro', component:RegistroComponent},
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
