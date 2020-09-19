import React,{useState} from 'react';
import InfiniteScroll from 'react-infinite-scroller';

import Search from '../search/Search';
import Video from './Video';
import ErrorMessage from '../utils/ErrorMessage';
import Loader from '../utils/Loader';

import fetchVideos from '../../utils/fetchVideos'

/** Videos Component - List all videos using a infinite scroll
 */
function Videos() {
  
  const [videos, setVideos] = useState([]);
  const [hasMoreVideos, setHasMoreVideos] = useState(false);
  const [query,setQuery] = useState(null);
  const [pageToken,setPageToken] = useState(null);
  const [errorMessage,setErrorMessage]= useState(null);

  const searchVideos = async(searchQuery) =>{
    if(searchQuery!=="" && searchQuery!==query){
      setVideos([]);
      setPageToken(null);
      setQuery(searchQuery);
      const data=await fetchVideos(searchQuery);
      if(!data.error){
        setVideos(data.videos);
        setErrorMessage(null);
        if(data.next_page_token) {
          setPageToken(data.next_page_token);
          setHasMoreVideos(true);
        }
      }else{
        setErrorMessage(data.error);
      }
    }
    
  }


  const loadItems=async(page) => {
    if(videos.length<200){
      let allVideos=videos;
      const data=await fetchVideos(query,pageToken);
      if(!data.error){
        for(const video of data.videos) allVideos.push(video);
        if(data.next_page_token) {
          setPageToken(data.next_page_token)
          if(videos.length>=200){
            setHasMoreVideos(false);

          }else{
            setHasMoreVideos(true);
          }
        }else{
          setHasMoreVideos(false);
        }
      }else{
        setHasMoreVideos(false);
      }
      
      setVideos(allVideos);
    }
  }
  return (
    <div>
      <Search searchVideos={searchVideos}></Search>
      <br/>
      {!errorMessage? 
      (
        <InfiniteScroll
          pageStart={0}
          loadMore={loadItems}
          hasMore={hasMoreVideos}
          loader={<Loader/>}
          >
          <div>
              {videos.map((video)=><Video key={video.id+Math.random()} video={video}/>)}
          </div>
        </InfiniteScroll>
      ):(
        <ErrorMessage errorMessage={errorMessage}/>
      )
    }
    </div>
  );
}

export default Videos;
