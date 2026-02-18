import { Injectable } from '@angular/core';
import Swal from 'sweetalert2';

@Injectable({
  providedIn: 'root',
})
export class AlertsService {
  showLoader(title:string="Cargando...",description:string="Espere unos segundos"):void{
    Swal.fire({
      title: title,
      text: description,
      showConfirmButton: false,
      allowOutsideClick: false,
      allowEscapeKey: false,
      didOpen: () => {
        Swal.showLoading()
      }
    })
  }

  confirm(title:string,description:string,confirmText:string="¿Estas seguro?",
          cancelText:string="Cancelar",icon:"warning"|"info"|"error"|"success"):void{
  }

  alert(title:string,description:string,icon:"warning"|"info"|"error"|"success"):void{
    Swal.fire({
      title: title,
      text: description,
      icon: icon,
      showConfirmButton: true,
      allowOutsideClick: true,
      confirmButtonText: "Cerrar notificacion",
    })
  }

  hide(){
    Swal.close()
  }
}
