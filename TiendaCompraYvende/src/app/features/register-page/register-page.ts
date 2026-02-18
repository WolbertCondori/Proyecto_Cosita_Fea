import {Component, inject, OnInit, signal} from '@angular/core';
import {Router} from '@angular/router';
import {FormBuilder, FormGroup, ReactiveFormsModule, Validators} from '@angular/forms';
import {emailValidator} from '../../core/validators/email.validator';
import {passwordValidator} from '../../core/validators/password.validator';
import {NgClass} from '@angular/common';
import {Users} from '../../core/services/users/users';
import {AlertsService} from '../../core/utils/alerts.service';

type datos={
  nombre?:string,
  email?:string,
  telefono?:string,
  nie?:string,
  nc?:string,
  password1?:string,
  password2?:string,
  fecha_nacimiento?:string,
  edad?:number,
  rol?:string,

}

@Component({
  selector: 'app-register-page',
  imports: [
    ReactiveFormsModule,
    NgClass
  ],
  templateUrl: './register-page.html',
  styleUrl: './register-page.scss',
})
export class RegisterPage{
  step = signal<boolean>(false);
  isPasswordVisible1 = signal<boolean>(false);
  isPasswordVisible2 = signal<boolean>(false);
  formBuilder = inject(FormBuilder);
  isPaciente=signal<boolean>(true)
  registerService = inject(Users)
  alertService = inject(AlertsService)

  formRegister = signal<FormGroup>(
    this.formBuilder.group({
      "nombre":["", [Validators.required]],
      "email": ["", [Validators.required, Validators.email, emailValidator]],
      "telefono":["",[]],
      "NIE":["",[Validators.required]],
      "NC":["",[]],
      "password1": ["", [Validators.required, Validators.minLength(4), passwordValidator]],
      "password2": ["", [Validators.required]],
      "fecha_nacimiento":["",[Validators.required]],
      "edad":["", [Validators.required]],
    }))



  constructor(private router: Router) {
    const navigation = this.router.currentNavigation()?.extras.state
    if (navigation) {
      this.isPaciente.set(navigation['isPaciente']);
    }
  }

  register() {
    if (this.formRegister()?.invalid) {
      alert("Formulario no válido");
      return;
    }
    if (this.formRegister()?.value.email === "") {
      alert("Falta ingresar un usuario")
      return;
    }
    const datos: datos={
      nombre: this.formRegister().value.nombre,
      email: this.formRegister().value.email,
      telefono: this.formRegister().value.telefono,
      nie: this.formRegister().value.NIE,
      nc: this.formRegister().value.NC,
      password1: this.formRegister().value.password1,
      password2: this.formRegister().value.password2,
      fecha_nacimiento: this.formRegister().value.fecha_nacimiento as string,
      edad: this.formRegister().value.edad as number,
      rol: this.isPaciente() ? "PAC" : "DOC"
    }
    console.log(datos);
    this.registerService.registro(datos).subscribe({
      next:(data)=> {
          this.alertService.showLoader()
      },
      error:(error)=> {
        this.alertService.alert("Error","La cuente no pudo crearse","error")
      },
      complete:()=>{
        this.router.navigateByUrl("/login").then();
        this.alertService.alert("Registrado","Tu cuenta fue creada con exito !!","success")
      }
    })
  }

  seePassword(n:number) {
    console.log(this.isPasswordVisible1());
    if (n==1) {
      this.isPasswordVisible1.update(state => !this.isPasswordVisible1());
    }
     if (n==2) {
      this.isPasswordVisible2.update(state=>!this.isPasswordVisible2())
    }
  }

  nextStep(){
    this.step.set(!this.step())
  }
}
