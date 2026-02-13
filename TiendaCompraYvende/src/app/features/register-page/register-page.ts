import {Component, inject, OnInit, signal} from '@angular/core';
import {Router} from '@angular/router';
import {FormBuilder, FormGroup, ReactiveFormsModule, Validators} from '@angular/forms';
import {emailValidator} from '../../core/validators/email.validator';
import {passwordValidator} from '../../core/validators/password.validator';
import {NgClass} from '@angular/common';

@Component({
  selector: 'app-register-page',
  imports: [
    ReactiveFormsModule,
    NgClass
  ],
  templateUrl: './register-page.html',
  styleUrl: './register-page.scss',
})
export class RegisterPage implements OnInit {
  step = signal<boolean>(false);
  isPasswordVisible1 = signal<boolean>(false);
  isPasswordVisible2 = signal<boolean>(false);
  formBuilder = inject(FormBuilder);
  isPaciente=signal<boolean>(true)

  formRegisterP = signal<FormGroup>(
    this.formBuilder.group({
      "nombre":["", [Validators.required]],
      "email": ["", [Validators.required, Validators.email, Validators.minLength(6), emailValidator]],
      "telefono":["",[]],
      "NIE":["",[Validators.required]],
      "password": ["", [Validators.required, Validators.minLength(4), passwordValidator]],
      "repeatPassword": ["", [Validators.required]],
      "fecha-nacimiento":["",[Validators.required]],
      "edad":["", [Validators.required]],
    }))

  formRegisterD = signal<FormGroup>(
    this.formBuilder.group({
      "nombre":["", [Validators.required]],
      "email": ["", [Validators.required, Validators.email, Validators.minLength(6), emailValidator]],
      "telefono":["",[]],
      "NIE":["",[Validators.required]],
      "NC":["",[Validators.required]],
      "password": ["", [Validators.required, Validators.minLength(4), passwordValidator]],
      "repeatPassword": ["", [Validators.required]],
      "fecha-nacimiento":["",[Validators.required]],
      "edad":["", [Validators.required]],
    }))



  constructor(private router: Router) {
    const navigation = this.router.currentNavigation()?.extras.state
    if (navigation) {
      this.isPaciente.set(navigation['isPaciente']);
    }
  }
  ngOnInit() {
    console.log(this.isPaciente());
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
