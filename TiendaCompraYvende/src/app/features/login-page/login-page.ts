import {Component, inject, output, signal} from '@angular/core';
import {FormBuilder, FormGroup, FormsModule, ReactiveFormsModule, Validators} from "@angular/forms";
import {emailValidator} from '../../core/validators/email.validator';
import {passwordValidator} from '../../core/validators/password.validator';
import {SesionDataService} from '../../core/services/sesion/sesion-data.service';
import {Router} from '@angular/router';
import {AuthCookieService} from '../../core/services/cookies/auth-cookie.service';
import {Users} from '../../core/services/users/users';
import {AlertsService} from '../../core/utils/alerts.service';

type datos={
  email?:string,
  password?:string
}



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
  formBuilder = inject(FormBuilder);
  route = inject(Router)
  sesionDataService = signal<SesionDataService | null>(null);
  authCookieService = inject(AuthCookieService)
  loginService = inject(Users)
  isPasswordVisible = signal<boolean>(false);
  alertService = inject(AlertsService)
  router = inject(Router)
  formLogin = signal<FormGroup>(
    this.formBuilder.group({
      "email": ["", [Validators.required, Validators.email, Validators.minLength(6), emailValidator]],
      "password": ["", [Validators.required, Validators.minLength(4), passwordValidator]],
    }))

  iniciarSesion() {
    if (this.formLogin()?.invalid) {
      alert("Formulario no válido");
      return;
    }
    if (this.formLogin()?.value.email === "") {
      alert("Falta ingresar un usuario")
      return;
    }

    const datosParaEnviar:datos ={
      email:this.formLogin()?.value.email,
      password:this.formLogin()?.value.password
    }
    this.loginService.login(datosParaEnviar).subscribe({
      next:(data)=>{
        console.log(data)
        this.authCookieService.set("MediPlus_token", data.data.token)
        this.authCookieService.set("MediPlus_refresh_token", data.data.refresh_token)
        this.authCookieService.set("user", data.data.nie)

        const datos:any={
          email:data.data.email,
          nombre:data.data.nombre
        }
        this.sesionDataService()?.set("MediPlus_Data",datos)
      },
      error:(err) => {
        this.alertService.alert("Error","No se pudo iniciar Sesion.","error")
      },
      complete:()=>{
        this.router.navigateByUrl("/main").then();
      }
    })
  }

  seePassword() {
    console.log(this.isPasswordVisible());
    this.isPasswordVisible.update(state => !this.isPasswordVisible());
  }
  changeToRegister(isPaciente:boolean){
    this.route.navigate(['/register'], {state: {isPaciente: isPaciente}})
   }
}
