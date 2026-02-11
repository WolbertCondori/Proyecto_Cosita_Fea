import { TestBed } from '@angular/core/testing';

import { SesionDataService } from './sesion-data.service';

describe('SesionDataService', () => {
  let service: SesionDataService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(SesionDataService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
