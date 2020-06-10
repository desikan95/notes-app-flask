import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { CardNotesComponent } from './card-notes/card-notes.component';
import { CreateNoteComponent } from './create-note/create-note.component'


const routes: Routes = [
  { path: 'cards',component: CardNotesComponent},
  { path: 'cards/new', component: CreateNoteComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
