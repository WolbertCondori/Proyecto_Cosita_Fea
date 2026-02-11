import { Routes } from '@angular/router';

export const routes: Routes = [
  {
    path:"",redirectTo:"login",pathMatch:"full",
  },
  {
    path:"login",loadComponent:()=>import("./features/login-page/login-page").then(c => c.LoginPage),
  },
  {
    path:"main",
    loadComponent:()=>import("./layouts/main-layout/main-layout").then((c)=>c.MainLayout),
    children:[
      {
        path:"",loadComponent:()=>import("./features/main-page/main-page").then((c)=>c.MainPage)
      },
      {
        path:"records",loadComponent:()=>import("./features/record-page/record-page").then((c)=>c.RecordPage)
      }
    ]
  },
  {
    path:"**",redirectTo:"page-not-found",pathMatch:"full",
  },
  {
    path:"page-not-found",loadComponent:()=>import("./features/page-not-found/page-not-found").then((c)=>c.PageNotFound)
  }
];
