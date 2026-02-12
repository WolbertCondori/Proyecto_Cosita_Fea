import { ComponentFixture, TestBed } from '@angular/core/testing';

import { LoginRegisterLayout } from './login-register-layout';

describe('LoginRegisterLayout', () => {
  let component: LoginRegisterLayout;
  let fixture: ComponentFixture<LoginRegisterLayout>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [LoginRegisterLayout]
    })
    .compileComponents();

    fixture = TestBed.createComponent(LoginRegisterLayout);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
