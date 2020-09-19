import React from 'react';
import {Container} from '@material-ui/core';
import logo from './logo.png';

import Videos from "./components/videos/Videos"
import './App.css';

function App() {
  
  
  return (
    <div className="App">
      <Container maxWidth="lg">
        <img src={logo} height={50}/>
        <Videos></Videos>
      </Container>
    </div>
  );
}

export default App;
