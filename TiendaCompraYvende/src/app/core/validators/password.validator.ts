import {AbstractControl, ValidationErrors} from '@angular/forms';


export function passwordValidator(password:AbstractControl):ValidationErrors|null{
  const value:string = password.value;
  if(!value||value==""){
    return null;
  }
  const regex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-z\d]{4,}$/i.test(value);
  return regex?null:{customPassword:true}
}
