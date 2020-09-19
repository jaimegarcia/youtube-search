import React from 'react';
import {Container} from '@material-ui/core';
import { makeStyles } from '@material-ui/core/styles';

import logo from './logo.png';

import Videos from "./components/videos/Videos"

const useStyles = makeStyles((theme) => ({
  logo: {
    textAlign: 'center'
  }
  }));

function App() {
  const classes = useStyles();

  
  return (

    <div className="App">
      <Container maxWidth="lg">
        <div className={classes.logo}><img src={logo} height={50} alt="Makrwatch"/></div>
        <Videos></Videos>
      </Container>
    </div>
  );
}

export default App;
