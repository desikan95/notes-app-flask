import { Component, OnInit } from '@angular/core';
// import { SAMPLE_NOTES } from '../sample-notes';
import { Notes } from '../notes';
import {NotesServiceService} from '../notes-service.service';
import { MessageService } from '../message.service';
import { Observable} from 'rxjs';

  declare var angular: any;

@Component({
  selector: 'app-card-notes',
  templateUrl: './card-notes.component.html',
  styleUrls: ['./card-notes.component.css']
})
export class CardNotesComponent implements OnInit {

  notes: Notes[];
  collapsed = true;
  textStyle: string;
  editStatus: boolean;
  action_1: string;
  action_2: string;
  temp_message: string;
  nothing_to_any: any;


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
      .subscribe(data =>{
                  //  this.notes = data.json();
                      console.log("Received ",data);
                //      var new_str = data.slice(1, -1);
                      this.notes =data;

                    //  this.nothing_to_any = JSON.parse(data);
                    //  console.log(" NOthing to any : ",this.nothing_to_any);
                //    this.noteob = Observable.from(data).toArray();
                      //this.notes = Array.of(this.notes);
      }
    );

    console.log(" Te value of this.notes : "+this.notes)
  }

  updatedValue(elem: HTMLInputElement): void {
    console.log(elem.value+" is the updated value");
    this.selectedNote.contents = elem.value;
  }

  onClickAction1(id: number): void {

    if(this.action_1=='edit')
    {

        console.log("Need to edit "+id);
        this.editStatus = true;

        this.action_1 = 'save';
        this.action_2 = 'cancel';

    }
    else
    {
        console.log("Need to save now");
        console.log("Edited message is "+this.selectedNote.contents);
        this.notesService.updateNote(this.selectedNote).subscribe(
          data => {
            console.log("This is what returned after put"+data);
          },
          () => console.log("Edited successfully")
        );
        this.action_1 = 'edit';
        this.action_2 = 'del';
    }
  }

  onClickAction2(id: number): void {

    if(this.action_2 == 'del')
    {

        console.log("Need to delete note "+id);

        this.notesService.deleteNote(id).subscribe(
          data => {
            console.log("This is what returned after delete"+data);
          },
          () => console.log("Deleted successfully")
        );

    }
    else
    {
        this.action_1 = 'edit';
        this.action_2 = 'del';
    }

  }

  ngOnInit(): void {
    this.getNoteItems();
    this.textStyle = 'editable';
    this.action_1 = 'edit';
    this.action_2 = 'del';
  }

}
