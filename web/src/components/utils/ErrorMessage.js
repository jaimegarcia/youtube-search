
import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import {Typography} from '@material-ui/core';


const useStyles = makeStyles(() => ({
  root: {
    textAlign: 'center'
  }
}));

/** Error Message Component
 * @param  {string} {errorMessage} Error Message
 */
export default function ErrorMessage({errorMessage}) {
  const classes = useStyles();
  return (

    <div className={classes.root}>
      <br/><br/>
      <Typography variant="h4">{errorMessage}</Typography>

    </div>
  );
}

