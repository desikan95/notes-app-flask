import { Injectable } from '@angular/core';
import { Notes } from './notes';
import { MessageService } from './message.service';
import { SAMPLE_NOTES } from './sample-notes';
import { Observable, of, throwError } from 'rxjs';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { retry, catchError } from 'rxjs/operators';
import { map } from "rxjs/operators";

@Injectable({
  providedIn: 'root'
})
export class NotesServiceService {

  private notesUrl = 'api/notes';

  constructor(
    private http: HttpClient,
    private messageService: MessageService
  ) { }

  httpOptions = {
  headers: new HttpHeaders({
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': '*',
    'Access-Control-Allow-Headers': '*'
  })
}

  getNotes(): Observable<Notes[]> {

    this.messageService.add('Notes Service: fetched noted');
    return this.http.get<Notes[]>('http://127.0.0.1/api/notes').pipe(
       map(res => res['notes'] || [])
    );

    }


  addNote(note: Notes): Observable<Notes> {
    return this.http.post<Notes>('http://127.0.0.1/api/notes', JSON.stringify(note), this.httpOptions);
  }

  updateNote(note: Notes): Observable<Notes> {

     return this.http.put<Notes>('http://127.0.0.1/api/notes', note, this.httpOptions);
  }

  deleteNote(id: Number): Observable<Notes> {
    const url = 'http://127.0.0.1/api/notes/'+id;
    return this.http.delete<Notes>(url, this.httpOptions);
  }


}
