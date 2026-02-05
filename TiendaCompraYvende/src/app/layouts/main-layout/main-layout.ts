import { Component } from '@angular/core';
import {HeadMain} from './components/head-main/head-main';
import {RouterOutlet} from '@angular/router';
import {FooterMain} from './components/footer-main/footer-main';

@Component({
  selector: 'app-main-layout',
  imports: [
    HeadMain,
    RouterOutlet,
    FooterMain
  ],
  templateUrl: './main-layout.html',
  styleUrl: './main-layout.scss',
})
export class MainLayout {

}
