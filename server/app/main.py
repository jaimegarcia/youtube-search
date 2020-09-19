import sys

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from key import api_key
from helpers import get_videos_ids,get_videos_data



app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]


version = f"{sys.version_info.major}.{sys.version_info.minor}"

MAX_RESULTS=50

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=["*"],
    allow_headers=["*"],
)

youtube = build('youtube', 'v3', developerKey=api_key)

@app.get("/api")
async def read_root():
    message = f"Hello world! From FastAPI running on Uvicorn with Gunicorn. Using Python {version}"
    return {"message": message}


@app.get("/api/search")
async def youtube_search(query: str = '',order: str = 'viewCount', pagetoken: str = None):
  """Get list of youtube videos from query including View Count
  Query Params:
    query (str): Video query term to search for
    order (str): Ordering criteria (relevance, date, rating, relevance, title, videoCount, viewCount) 
    pagetoken (str): Indentifies a specific page in the results to be returned 
  Returns:
      [json]: [Returns video list, previous and next page token]
  """

  search_response = youtube.search().list(q=query, part='snippet', type='video', maxResults=MAX_RESULTS, order=order,pageToken=pagetoken).execute()
  
  videos_ids=get_videos_ids(search_response)
  if videos_ids=="":
    return {"error":"No videos match the query"}

  statistics_response = youtube.videos().list(part='statistics', id=videos_ids).execute()

  videos_data=get_videos_data(search_response,statistics_response)


  return {"videos":videos_data,"prev_page_token":search_response.get('prevPageToken'),"next_page_token":search_response.get('nextPageToken')}