import {Component, input, OnInit, signal} from '@angular/core';
import {Router} from '@angular/router';

@Component({
  selector: 'app-register-page',
  imports: [],
  templateUrl: './register-page.html',
  styleUrl: './register-page.scss',
})
export class RegisterPage{
  isPaciente:boolean=false;
  constructor(private router: Router) {
    const navigation = this.router.currentNavigation()?.extras.state
    if (navigation) {
      this.isPaciente = navigation['isPaciente'];
    }
  }
}
