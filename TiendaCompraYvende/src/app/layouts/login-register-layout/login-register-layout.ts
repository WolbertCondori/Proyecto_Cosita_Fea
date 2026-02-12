import {Component, input, signal} from '@angular/core';
import {FormsModule, ReactiveFormsModule} from "@angular/forms";
import {RouterOutlet} from '@angular/router';

@Component({
  selector: 'app-login-register-layout',
  imports: [
    FormsModule,
    ReactiveFormsModule,
    RouterOutlet
  ],
  templateUrl: './login-register-layout.html',
  styleUrl: './login-register-layout.scss',
})
export class LoginRegisterLayout {
}
