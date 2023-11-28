import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { InicioPaginaComponent } from './inicio-pagina/inicio-pagina.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { AdminComponent } from './admin/admin.component';
import { LoginComponent } from './login/login.component';
import { RegistroComponent } from './registro/registro.component';
import { CreacionEstampaComponent } from './creacion-estampa/creacion-estampa.component';
import { PersonalizacionCamisetaComponent } from './personalizacion-camiseta/personalizacion-camiseta.component';

@NgModule({
    declarations: [
        AppComponent,
        InicioPaginaComponent,
        AdminComponent,
        LoginComponent,
        RegistroComponent,
        CreacionEstampaComponent,
        PersonalizacionCamisetaComponent
    ],
    providers: [],
    bootstrap: [AppComponent],
    imports: [
        BrowserModule,
        AppRoutingModule,
        NgbModule,
        ReactiveFormsModule,
        HttpClientModule,
        FormsModule
    ]
})
export class AppModule { }
