import { Component } from '@angular/core';
import {Router, RouterLink} from '@angular/router';

@Component({
  selector: 'app-head-main',
  imports: [
    RouterLink
  ],
  templateUrl: './head-main.html',
  styleUrl: './head-main.scss',
})
export class HeadMain {
  constructor(private router: Router) {}


}
