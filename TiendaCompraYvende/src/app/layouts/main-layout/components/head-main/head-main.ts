import {Component, signal} from '@angular/core';
import {Router, RouterLink} from '@angular/router';
import {LoginMain} from '../login-main/login-main';

@Component({
  selector: 'app-head-main',
  imports: [
    RouterLink,
    LoginMain
  ],
  templateUrl: './head-main.html',
  styleUrl: './head-main.scss',
})
export class HeadMain {
  openLogin = signal<boolean>(false)
  constructor(private router: Router) {}

  openedLogin(): void {
    this.openLogin.update(state=>!state);
  }

}
