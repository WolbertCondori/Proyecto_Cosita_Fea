import { Injectable } from '@angular/core';
import {Observable} from 'rxjs';
import {HttpClient} from '@angular/common/http';
import {environment} from '../../../../environments/enviroment';

@Injectable({
  providedIn: 'root',
})
export class Users {
  private URL = environment.apiURL;

  constructor(private http:HttpClient) {
  }
  registro(datos:any):Observable<any>{
    return this.http.post<any>(`${this.URL}/RegisterUsers/`,datos)
  }
  login(datos:any):Observable<any>{
    return this.http.post<any>(`${this.URL}/LoginUsers/`,datos)
  }
  get_users():Observable<any>{
    return this.http.get<any>(`${this.URL}/RegisterUsers/`)
  }
  get_user(datos:any):Observable<any>{
    return this.http.get<any>(`${this.URL}/RegisterUsers/`, {params: datos})
  }
}
