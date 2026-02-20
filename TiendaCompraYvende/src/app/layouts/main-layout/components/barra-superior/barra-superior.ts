import {Component, inject, OnInit, signal} from '@angular/core';
import {Users} from '../../../../core/services/users/users';

import {AuthCookieService} from '../../../../core/services/cookies/auth-cookie.service';

@Component({
  selector: 'app-barra-superior',
  imports: [],
  templateUrl: './barra-superior.html',
  styleUrl: './barra-superior.scss',
})
export class BarraSuperior implements OnInit {
  userService = inject(Users)
  cookieService = inject(AuthCookieService);
  user_data=signal<any>(null)
  ngOnInit(): void {
    const datos={
      user:this.cookieService.get("user")
    }
    this.userService.get_user(datos).subscribe({
      next: data => {
        this.user_data.set(data.data)
      }
    })
  }
}
