import { Component } from '@angular/core';
import {CargarScriptsService} from "./../servicios/cargar-scripts.service";

@Component({
  selector: 'app-inicio',
  templateUrl: './inicio-pagina.component.html',
  styleUrls: ['./inicio-pagina.component.css','../css/bootstrap.css','../css/fontawesome-all.css','../css/login_overlay.css','../css/owl.carousel.css','../css/owl.theme.css',
              '../css/shop.css','../css/style.css','../css/style6.css']
})
export class InicioPaginaComponent {
  images = ["logo.png","s1.jpg","s2.jpg","s3.jpg","s4.jpg","m1.jpg","m2.jpg","m3.jpg","m4.jpg","s5.jpg","s6.jpg","s7.jpg","s8.jpg","s9.jpg","s10.jpg","banner4.jpg","banner3.jpg"].map((n) => `assets/images/${n}`);
  constructor(private _CargaScripts:CargarScriptsService)
  {
    _CargaScripts.Carga(["jquery-2.2.3.min","jquery-ui","jquery.easing.min","jquery.flexslider","jquery.magnific-popup","bootstrap","modernizr-2.6.2.min","classie-search","creditly","demo1-search","easing","easy-responsive-tabs","imagezoom","minicart","move-top","owl.carousel","simplyCountdown"])
  }
  
}