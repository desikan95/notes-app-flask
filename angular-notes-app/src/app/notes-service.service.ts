import { Injectable } from '@angular/core';
import { Notes } from './notes';
import { MessageService } from './message.service';
import { SAMPLE_NOTES } from './sample-notes';
import { Observable, of } from 'rxjs';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class NotesServiceService {

  private notesUrl = 'api/notes';

  constructor(
    private http: HttpClient,
    private messageService: MessageService
  ) { }

  getNotes(): Observable<Notes[]> {

    this.messageService.add('Notes Service: fetched noted');
    return this.http.get<Notes[]>(this.notesUrl);
  }
}
