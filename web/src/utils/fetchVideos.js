import { searchAPI } from "../config/config";
import axios from 'axios';



/** Fetch Video List from Backend
 * @param  {String} query Video query term to search for
 * @param  {String} pageToken Indentifies a specific page in the results to be returned 
 * @param  {String} order Ordering criteria (relevance, date, rating, relevance, title, videoCount, viewCount) 
 */
const fetchVideos = async(query,pageToken,order) =>{

  let params={query};
  if(order) params.order=order;
  if(pageToken) params.pagetoken=pageToken;

  const res = await axios.get(searchAPI, { params});
  return res.data;
}

export default fetchVideos;