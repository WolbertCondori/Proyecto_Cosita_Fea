import {Component, inject, OnInit, signal} from '@angular/core';
import {Citas} from '../../core/services/citas/citas';
import {AlertsService} from '../../core/utils/alerts.service';
import {AuthCookieService} from '../../core/services/cookies/auth-cookie.service';

interface CitaInterface{
  nie:string;
  fecha:string;
  estado:string;
  creado:string;
  slug:string;
}

@Component({
  selector: 'app-citas-page',
  imports: [],
  templateUrl: './citas-page.html',
  styleUrl: './citas-page.scss',
})
export class CitasPage implements OnInit {

    citas = signal<CitaInterface[]>([])

    citasService = inject(Citas)
    alertService = inject(AlertsService)
    authCookieService = inject(AuthCookieService)



    ngOnInit(): void {
      this.alertService.showLoader();
      const datos={
        user:this.authCookieService.get("user")
      }
      setTimeout(() => {
        this.citasService.get_Citas(datos).subscribe({
          next: data => {
            this.citas.set(data.data);
          },
          error: err => {
            this.alertService.alert("Error De Conexion","Problemas al conectar con la base de datos","error");
          },
          complete: () => {
            this.alertService.hide();
          }
        })
      }, 3000)
    }

    createCita(){

    }

    recharged(){
      this.ngOnInit()
    }
}
