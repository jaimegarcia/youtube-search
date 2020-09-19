import React from 'react';
import { makeStyles, useTheme } from '@material-ui/core/styles';
import {Card,CardContent,CardMedia,Typography} from '@material-ui/core';
import moment from "moment";

const useStyles = makeStyles((theme) => ({
  root: {
    display: 'flex',
    marginBottom: 30
  },
  details: {
    display: 'flex',
    flexDirection: 'column',
  },
  content: {
    flex: '1 0 auto',
  },
  cover: {
    width: 320,
    height: 180
  }
}));

export default function Video({video}) {
  const classes = useStyles();
  return (
    <Card className={classes.root} elevation={0}>
        <img
        src={video.image}
      />
      <div className={classes.details}>
        <CardContent className={classes.content}>
          <Typography component="h5" variant="h5">
            {video.title}
          </Typography>
          <Typography component="h5" variant="h5">
            {video.channel_title}
          </Typography>
          <Typography variant="h5" color="textSecondary">
          {video.view_count}
          </Typography>
          <Typography variant="h5" color="textSecondary">
          {moment(video.published_at).startOf("hour").fromNow()}
          </Typography>
        </CardContent>
      </div>

    </Card>
  );
}