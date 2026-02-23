import {Component} from '@angular/core';

@Component({
  selector: 'app-root',
  template: ` @if (isLoggedIn) {
    <p>Welcome back, Friend!</p>
  } `,
})
export class App {
  isLoggedIn = true;
}