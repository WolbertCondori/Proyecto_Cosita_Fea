import {inject, Injectable} from '@angular/core';
import {CookieService} from 'ngx-cookie-service';

@Injectable({
  providedIn: 'root',
})
export class AuthCookieService {
  constructor(private cookieService: CookieService) {
  }

  /// Obtener Cookie

  get(key: string) {
    return this.cookieService.get(key); // key = name and just return value
  }

  /// Crear/Modificar Cookie

  set(key: string, value: any, days: number = 7) {
    this.cookieService.set(
      key,
      value,
      days,
      "/",//Esto vale para que toda pagina funcione
      undefined, false,//Solo permitimos HTTPS?
      "Lax"
    );
  }

  /// Borrar Cookie

  remove(key:string){
    this.cookieService.delete(key)
  }

  /// Comprobar Cookie Existente

  exists(key:string):boolean{
    return this.cookieService.check(key)
  }

  /// Borrar todas las Cookies

  removeAll():void{
    this.cookieService.deleteAll()
  }


}
