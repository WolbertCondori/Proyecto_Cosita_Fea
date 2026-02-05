import { Routes } from '@angular/router';

export const routes: Routes = [
  {
    path:"",redirectTo:"main",pathMatch:"full",
  },
  {
    path:"main",
    loadComponent:()=>import("./layouts/main-layout/main-layout").then((c)=>c.MainLayout),
    children:[
      {
        path:"main",loadComponent:()=>import("./features/main-page/main-page").then((c)=>c.MainPage)
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
