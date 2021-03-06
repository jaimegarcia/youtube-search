import html

def get_videos_ids(search_response):
  """Extract videos ids from search response

  Args:
      search_response (dict): Response from search query

  Returns:
      str: String separated by commas with ids of the videos
  """
  videos_ids=[]
  for item in search_response.get('items', []):
    videos_ids.append(item['id']['videoId'])
  
  return ",".join(videos_ids)

def get_videos_data(search_response,statistics_response):
  """Generates video list from youtube search and video statistics responses, removing all unnecesary fields

  Args:
      search_response (dict): Response from search query
      statistics_response (dict): Response from search query

  Returns:
      list: List of videos for displaying in the front  
  """
  videos_data=[]
  for snippet, statistics in zip(search_response.get('items', []), statistics_response.get('items', [])):
    video=dict()
    video["id"]=snippet["id"]["videoId"]
    video["title"]=html.unescape(snippet["snippet"]["title"])
    video["description"]=html.unescape(snippet["snippet"]["description"])
    video["channel_title"]=html.unescape(snippet["snippet"]["channelTitle"])
    video["image_low_res"]=snippet["snippet"]["thumbnails"]["medium"]["url"]
    video["image_high_res"]=snippet["snippet"]["thumbnails"]["high"]["url"]
    video["published_at"]=snippet["snippet"]["publishedAt"]
    video["view_count"]=statistics["statistics"]["viewCount"]
    videos_data.append(video)

  return videos_data