import { ComponentFixture, TestBed } from '@angular/core/testing';

import { HeadMain } from './head-main';

describe('HeadMain', () => {
  let component: HeadMain;
  let fixture: ComponentFixture<HeadMain>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [HeadMain]
    })
    .compileComponents();

    fixture = TestBed.createComponent(HeadMain);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
