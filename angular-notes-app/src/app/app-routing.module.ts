import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { CardNotesComponent } from './card-notes/card-notes.component';


const routes: Routes = [
  { path: 'cards',component: CardNotesComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
