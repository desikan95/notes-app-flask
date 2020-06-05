import { Component, OnInit } from '@angular/core';
// import { SAMPLE_NOTES } from '../sample-notes';
import { Notes } from '../notes';
import {NotesServiceService} from '../notes-service.service';
import { MessageService } from '../message.service';

@Component({
  selector: 'app-card-notes',
  templateUrl: './card-notes.component.html',
  styleUrls: ['./card-notes.component.css']
})
export class CardNotesComponent implements OnInit {

  notes: Notes[];
  collapsed = true;

  selectedNote: Notes;
  onSelect(note: Notes): void {
    this.selectedNote = note;
    this.messageService.add(`Notes Service : Selected note id=${note.id}`);
  }
  deSelect(note: Notes): void {
    this.selectedNote= null;
  }

  constructor(private notesService: NotesServiceService, private messageService: MessageService) {}

  getNoteItems(): void {
  //  this.notes = this.notesService.getNotes();

    this.notesService.getNotes()
      .subscribe(notes => this.notes = notes);
  }

  ngOnInit(): void {
    this.getNoteItems();
  }

}
