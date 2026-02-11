import {CanActivateFn, Router} from '@angular/router';
import {AuthCookieService} from '../services/cookies/auth-cookie.service';
import {inject} from '@angular/core';

export const authGuard: CanActivateFn = (route, state) => {
  const router = inject(Router)
  const cookieService = inject(AuthCookieService);
  const valor = cookieService.get('login');
  if (!valor) {
    router.navigate(['/page-not-found']);
    return false;
  }else {
    return true;
  }
};
