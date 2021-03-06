import React from 'react';
import render from 'react-dom';
// import './index.css';
import App from './App';
import { ThemeProvider } from '@material-ui/styles'
import Theme from "./components/Theme";
// import * as serviceWorker from './serviceWorker';

render((
  <ThemeProvider theme={Theme}>
    <App />
  </ThemeProvider>),
  document.getElementById('root'));

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
// serviceWorker.unregister();
