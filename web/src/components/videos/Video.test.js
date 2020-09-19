import React from 'react'
import { render } from '@testing-library/react';
import Video from './Video'

describe('Video', () => {


  it('should render video from data', () => {

    const video={
      "id": "ZAxhEUfpSss",
      "title": "Trying TJ MAXX Makeup For The First Time",
      "description": "HEY EVERYONE... Welcome BACK to my channel! Today I go to TJ MAXX for the first time in 10 years and try to find a full face of makeup! Follow me on this ...",
      "channel_title": "jeffreestar",
      "image_low_res": "https://i.ytimg.com/vi/ZAxhEUfpSss/mqdefault.jpg",
      "image_high_res": "https://i.ytimg.com/vi/ZAxhEUfpSss/hqdefault.jpg",
      "published_at": "2019-02-22T17:59:38Z",
      "view_count": "23965302"
    }
    
    const { getByText, getByRole } = render(<Video video={video} />)


    expect(getByText(/Trying TJ MAXX Makeup For The First Time/i)).toBeInTheDocument(); //Should render Title
    expect(getByText(/jeffreestar/i)).toBeInTheDocument(); //Should render Channel Title
    expect(getByText(/2 years ago/i)).toBeInTheDocument(); //Should calculate date from publish date and show it in proper format
    expect(getByText(/23,965,302 Views/i)).toBeInTheDocument(); //Should render views with thousand separator
    expect(getByRole('link')).toHaveAttribute('href', 'https://www.youtube.com/watch?v=ZAxhEUfpSss') //Should generate link to video

  })

});