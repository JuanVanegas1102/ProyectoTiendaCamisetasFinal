import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CreacionEstampaComponent } from './creacion-estampa.component';

describe('CreacionEstampaComponent', () => {
  let component: CreacionEstampaComponent;
  let fixture: ComponentFixture<CreacionEstampaComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CreacionEstampaComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CreacionEstampaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
