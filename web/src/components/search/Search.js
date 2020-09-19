import React,{useState} from 'react';
import { makeStyles } from '@material-ui/core/styles';

import { Button, TextField} from '@material-ui/core';
import SearchIcon from '@material-ui/icons/Search';

const useStyles = makeStyles((theme) => ({
  root: {
    padding: '2px 4px',
    textAlign: 'center'
  },
  input: {
    marginLeft: theme.spacing(1),
    maxWidth:600,
    width:'70%',
    flex: 1,
  },
  iconButton: {
    paddingTop: 8,
    paddingBottom:4,
    paddingLeft: 14,
    paddingRight:0,
    backgroundColor:'#4BA5AA',
    "&:hover": {
      backgroundColor:'#3b7c7f'
    }
  },
  searchIcon:{
    marginLeft:0,
    fontSize:'43px!important',
    color:'white'
  }
}));

/** Search Component - Triggers the fetch in the Videos Component sending the search query
 * @param  {Function} {searchVideos}
 */
export default function Search({searchVideos}) {
  const classes = useStyles();

  const [searchQuery, setSearchQuery] = useState("")


  return (
    <div className={classes.root}>
      <TextField
        className={classes.input}
        variant="outlined" 
        placeholder="Search topics on the videos you want to find"
        inputProps={{ 'aria-label': 'search topics on the videos' }}
        onChange={(event)=> setSearchQuery(event.target.value)}
      />
      <Button onClick={() =>searchVideos(searchQuery)} className={classes.iconButton} aria-label="search" variant="contained" startIcon={<SearchIcon className={classes.searchIcon}/>}>
      </Button>
    </div>
  );
}

