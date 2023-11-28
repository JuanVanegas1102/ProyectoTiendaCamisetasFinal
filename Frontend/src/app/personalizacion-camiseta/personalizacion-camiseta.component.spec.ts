import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PersonalizacionCamisetaComponent } from './personalizacion-camiseta.component';

describe('PersonalizacionCamisetaComponent', () => {
  let component: PersonalizacionCamisetaComponent;
  let fixture: ComponentFixture<PersonalizacionCamisetaComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PersonalizacionCamisetaComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(PersonalizacionCamisetaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
