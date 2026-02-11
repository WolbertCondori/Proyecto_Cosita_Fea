import {Component, inject, output, signal} from '@angular/core';
import {FormBuilder, FormGroup, FormsModule, ReactiveFormsModule, Validators} from "@angular/forms";
import {emailValidator} from '../../core/validators/email.validator';
import {passwordValidator} from '../../core/validators/password.validator';
import {SesionDataService} from '../../core/services/sesion/sesion-data.service';

@Component({
  selector: 'app-login-page',
    imports: [
        FormsModule,
        ReactiveFormsModule
    ],
  templateUrl: './login-page.html',
  styleUrl: './login-page.scss',
})
export class LoginPage {
  closeLoginForm = output();
  formBuilder = inject(FormBuilder);
  isPasswordVisible = signal<boolean>(false);
  formLogin = signal<FormGroup>(
    this.formBuilder.group({
      "email": ["", [Validators.required, Validators.email, Validators.minLength(6), emailValidator]],
      "password": ["", [Validators.required, Validators.minLength(4), passwordValidator]],
    }))
  sesionDataService = signal<SesionDataService | null>(null);

  iniciarSesion() {
    if (this.formLogin()?.invalid) {
      alert("Formulario no válido");
      return;
    }
    if (this.formLogin()?.value.email === "") {
      alert("Falta ingresar un usuario")
      return;
    }

    //const datosParaEnviar:DatosDeEnvio ={
    //  email:this.formLogin.value.email,
    //  telefono:this.formLogin.value.telefono,
    //  password:this.formLogin.value.password
    //}
    //this.authService.login(datosParaEnviar).subscribe({
    //  next:(data)=>{
    //    console.log(data)
    //    this.authCookieService.set("tienda_online_token", data.data.token)
    //    this.authCookieService.set("tienda_online_refresh_token", data.data.refresh_token)
//
    //    const datos:any={
    //      email:data.data.email,
    //      nombre:data.data.nombre
    //    }
    //    this.sesionDataService()?.set("tienda_online_datos",datos)
    //  },
    //  error:(err) => {
    //    console.log(err)
    //  }
    //})
  }

  seePassword() {
    console.log(this.isPasswordVisible());
    this.isPasswordVisible.update(state => !this.isPasswordVisible());
  }
}
