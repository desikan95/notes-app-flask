import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators} from '@angular/forms';
import {NotesServiceService} from '../notes-service.service';
import { Notes } from '../notes';
import { Router } from '@angular/router';

@Component({
  selector: 'app-create-note',
  templateUrl: './create-note.component.html',
  styleUrls: ['./create-note.component.css']
})
export class CreateNoteComponent implements OnInit {

  messageForm: FormGroup;
  submitted = false;
  success = false;
  form_note: Notes;
  notes: Notes[];

  constructor(private formBuilder: FormBuilder,private notesService: NotesServiceService, private router: Router)
  {
    this.messageForm = this.formBuilder.group({
      topic: ['',Validators.required],
      contents: ['',Validators.required],
      id: ['',Validators.required]
    });

  }



  onSubmit(){
    this.submitted = true;

    if (this.messageForm.invalid) {
      return;
    }
    console.log(this.messageForm.controls.contents.value);
    this.notesService.addNote(this.messageForm.value).subscribe(
      data => {
        console.log(" Item added ");
        this.router.navigateByUrl('/cards');
      }
    );


    this.success = true;

  }

  ngOnInit(): void {
  }

}
