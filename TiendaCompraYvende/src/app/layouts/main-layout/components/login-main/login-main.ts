import {Component, output, signal} from '@angular/core';
import {FormBuilder, FormGroup, ReactiveFormsModule, Validators} from '@angular/forms';

@Component({
  selector: 'app-login-main',
  imports: [
    ReactiveFormsModule
  ],
  templateUrl: './login-main.html',
  styleUrl: './login-main.scss',
})
export class LoginMain {
  closeLoginForm =output();
  formLogin=signal<FormGroup|null>(null);
  constructor(private formBuilder: FormBuilder) {
    this.formLogin.set(this.formBuilder.group({
      "email":["",[Validators.email,Validators.minLength(5)]],
      "password":["",[Validators.required,Validators.minLength(6)]],
    }))
  }
}
