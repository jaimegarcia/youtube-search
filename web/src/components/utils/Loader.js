
import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import CircularProgress from '@material-ui/core/CircularProgress';


const useStyles = makeStyles(() => ({
  root: {
    textAlign: 'center'
  }
}));

/** Loader Component
 * 
 */
export default function Loader() {
  const classes = useStyles();
  return (

    <div className={classes.root}>
      <br/><br/>
      <CircularProgress color="secondary"/>

    </div>
  );
}




