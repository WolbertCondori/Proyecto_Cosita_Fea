import { Component } from '@angular/core';
import {RouterLink, RouterOutlet} from '@angular/router';
import {BarraLateral} from './components/barra-lateral/barra-lateral';
import {BarraSuperior} from './components/barra-superior/barra-superior';

@Component({
  selector: 'app-main-layout',
  imports: [
    RouterOutlet,
    BarraLateral,
    BarraSuperior
  ],
  templateUrl: './main-layout.html',
  styleUrl: './main-layout.scss',
})
export class MainLayout {

}
