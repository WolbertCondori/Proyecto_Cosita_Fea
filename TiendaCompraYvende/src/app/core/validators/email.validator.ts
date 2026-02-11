import {AbstractControl, ValidationErrors} from '@angular/forms';

export function emailValidator(email:AbstractControl):ValidationErrors|null{
  const value:string = email.value;
  if(!value||value==''){
    return null;
  }
  const regex = /^[a-z\d._-]{3,}(@)(gmail|hotmail|doe)[a-z.]*$/i.test(value);
  if(!regex) {
    return {emailValidator: true}
  }
  const regex2 =  /^[a-z\d._-]{3,}(@)(gmail|hotmail|doe)(\.)(com|es)$/i.test(value);
  return regex2 ? null:{extention:true}
}
