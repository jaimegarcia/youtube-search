import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import {Box,Card,CardContent,Typography} from '@material-ui/core';
import { grey } from '@material-ui/core/colors';

import moment from "moment";

import formatViewCount from '../../utils/formatViewCount'

const useStyles = makeStyles((theme) => ({
  root: {
    marginBottom: 30,
    [theme.breakpoints.up('sm')]:{
      display: 'flex'
    } 
  },
  details: {
    display: 'flex',
    flexDirection: 'column',
  },
  content: {
    flex: '1 0 auto',
    paddingTop:0
  },
  videoTitle:{
    lineHeight:1.2
  },
  smallImage: {
    width: 320,
    height: 180
  },
  bigImage:{
    width: '100%'
  },
  channelTitle:{
    color: grey['700']
  },
  viewCount:{
    backgroundColor:"#4BA5AA",
    color:"white",
    padding:2
  }
}));

/** Video Item Component - Display Card with link, image, title, channel, view Count, Publishabled date and description
 * @param  {Object} {video}
 */
export default function Video({video}) {
  const classes = useStyles();
  return (
    <a href={`https://www.youtube.com/watch?v=${video.id}`} target="_blank" rel="noopener noreferrer" style={{ textDecoration: 'none' }}>

      <Card className={classes.root} elevation={0}>
        <Box display={{ xs: 'none',sm:'block' }} >
          <img display={{ xs: 'none'}} className={classes.smallImage} alt={video.title} src={video.image_low_res} />
        </Box>
        <div className={classes.details}>
          <CardContent className={classes.content}>
          <Box display={{ xs: 'block', sm: 'none' }} >
            <img alt={video.title} src={video.image_high_res} className={classes.bigImage} />
          </Box>
            <Typography variant="h6" className={classes.videoTitle}>
              {video.title}
            </Typography>
            <Typography variant="subtitle2" className={classes.channelTitle}>
              {video.channel_title}
            </Typography>
            <Typography variant="subtitle1" color="textSecondary">
            <span className={classes.viewCount}>{`${formatViewCount(video.view_count)} Views`}</span> • {moment(video.published_at).startOf("hour").fromNow()}
            </Typography>
            <br/>
            <Typography variant="subtitle2" >
              <Box display={{ xs: 'none',sm:'none',md:'block' }} >{video.description}</Box>
            </Typography>
            <br/>
          </CardContent>
        </div>
      </Card>
    </a>
  );
}