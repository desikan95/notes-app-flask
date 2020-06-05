import { Injectable } from '@angular/core';
import { Notes } from './notes';
import { MessageService } from './message.service';
import { SAMPLE_NOTES } from './sample-notes';
import { Observable, of } from 'rxjs';


@Injectable({
  providedIn: 'root'
})
export class NotesServiceService {

  constructor(private messageService: MessageService) { }

  getNotes(): Observable<Notes[]> {

    this.messageService.add('Notes Service: fetched noted');
    return of(SAMPLE_NOTES);
  }
}
