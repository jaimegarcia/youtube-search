import React,{useState} from 'react';
import { fade,makeStyles, useTheme } from '@material-ui/core/styles';

import { InputBase,Button, TextField} from '@material-ui/core';
import SearchIcon from '@material-ui/icons/Search';

const useStyles = makeStyles((theme) => ({
  root: {
    padding: '2px 4px',
    display: 'flex',
    alignItems: 'center',
    width: 400,
  },
  input: {
    marginLeft: theme.spacing(1),
    flex: 1,
  },
  iconButton: {
    paddingTop: 30,
    background:"#4BA5AA"
  },
  divider: {
    height: 28,
    margin: 4,
  },
  searchIcon:{
    marginLeft:0
  }
}));

export default function Search({searchVideos}) {
  const classes = useStyles();

  const [searchQuery, setSearchQuery] = useState("")


  return (
    <React.Fragment>
      <TextField
        className={classes.input}
        fullWidth
        variant="outlined" 
        placeholder="Search topics on the videos you want to find"
        inputProps={{ 'aria-label': 'search topics on the videos' }}
        onChange={(event)=> setSearchQuery(event.target.value)}
      />
      <Button onClick={() =>searchVideos(searchQuery)} className={classes.iconButton} aria-label="search" variant="contained" startIcon={<SearchIcon className={classes.searchIcon}/>}>
      </Button>
    </React.Fragment>
  );
}

