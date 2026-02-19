import { Injectable } from '@angular/core';
import {environment} from '../../../../environments/enviroment';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class Citas {
  private URL = environment.apiURL;

  constructor(private http:HttpClient) {
  }
  createCita(datos:any):Observable<any>{
    return this.http.post<any>(`${this.URL}/Citas/`,datos)
  }
  get_Citas(datos:any):Observable<any>{
    return this.http.get<any>(`${this.URL}/Citas/`, {params: datos})
  }
}
