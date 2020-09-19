import unittest
from helpers import get_videos_ids,get_videos_data
class TestYoutubeSearchHelpers(unittest.TestCase):

  def test_get_videos_ids(self):

    search_response={
      "kind": "youtube#searchListResponse",
      "etag": "v6dM80l-6N7XAw0vC_a-ke30Yq4",
      "nextPageToken": "CAoQAA",
      "regionCode": "CO",
      "pageInfo": {
        "totalResults": 1000000,
        "resultsPerPage": 10
      },
      "items": [{
        "kind": "youtube#searchResult",
        "etag": "EMdBOdJXt9T87j1Sa-bnMKlCKuw",
        "id": {
          "kind": "youtube#video",
          "videoId": "gSa0e34EZyQ"
        },
        "snippet": {
          "publishedAt": "2019-06-16T06:30:05Z",
          "channelId": "UCt_KDu-DtBqvIw7X-V7mlmQ",
          "title": "Pari&#39;s Magical Beauty Parlour | Pari Doing Makeup | Funny Video",
          "description": "In today's Video i have opened a Beauty Parlour and i am doing very beautiful makeup of customers . So watch it and enjoy. Links to buy the products = 1. Magic ...",
          "thumbnails": {
            "default": {
              "url": "https://i.ytimg.com/vi/gSa0e34EZyQ/default.jpg",
              "width": 120,
              "height": 90
            },
            "medium": {
              "url": "https://i.ytimg.com/vi/gSa0e34EZyQ/mqdefault.jpg",
              "width": 320,
              "height": 180
            },
            "high": {
              "url": "https://i.ytimg.com/vi/gSa0e34EZyQ/hqdefault.jpg",
              "width": 480,
              "height": 360
            }
          },
          "channelTitle": "Pari's Lifestyle",
          "liveBroadcastContent": "none",
          "publishTime": "2019-06-16T06:30:05Z"
        }
      }, {
        "kind": "youtube#searchResult",
        "etag": "HwLipIMdNkx-iPl9AxDMSQf0zIo",
        "id": {
          "kind": "youtube#video",
          "videoId": "YxoSmwXhvdw"
        },
        "snippet": {
          "publishedAt": "2015-09-13T05:10:15Z",
          "channelId": "UCQ2WjcRRelz7iLn9s0igjww",
          "title": "Giant Surprise Egg 1 - Barbie, Monster High, Peppa Pig, and Play Doh - Toys R Us Shopping Spree",
          "description": "Giant Surprise Egg 1 is the first in a new series from Kaylee Bug Tv. Kaylee goes shopping for Barbie, Monster High, Peppa Pig, Play Doh, and more. All of these ...",
          "thumbnails": {
            "default": {
              "url": "https://i.ytimg.com/vi/YxoSmwXhvdw/default.jpg",
              "width": 120,
              "height": 90
            },
            "medium": {
              "url": "https://i.ytimg.com/vi/YxoSmwXhvdw/mqdefault.jpg",
              "width": 320,
              "height": 180
            },
            "high": {
              "url": "https://i.ytimg.com/vi/YxoSmwXhvdw/hqdefault.jpg",
              "width": 480,
              "height": 360
            }
          },
          "channelTitle": "Kaylee Bug Tv",
          "liveBroadcastContent": "none",
          "publishTime": "2015-09-13T05:10:15Z"
        }
      }, {
        "kind": "youtube#searchResult",
        "etag": "Cbh94n-zyeVW_Boc4F1AU7w4DEw",
        "id": {
          "kind": "youtube#video",
          "videoId": "ZAxhEUfpSss"
        },
        "snippet": {
          "publishedAt": "2019-02-22T17:59:38Z",
          "channelId": "UCkvK_5omS-42Ovgah8KRKtg",
          "title": "Trying TJ MAXX Makeup For The First Time",
          "description": "HEY EVERYONE... Welcome BACK to my channel! Today I go to TJ MAXX for the first time in 10 years and try to find a full face of makeup! Follow me on this ...",
          "thumbnails": {
            "default": {
              "url": "https://i.ytimg.com/vi/ZAxhEUfpSss/default.jpg",
              "width": 120,
              "height": 90
            },
            "medium": {
              "url": "https://i.ytimg.com/vi/ZAxhEUfpSss/mqdefault.jpg",
              "width": 320,
              "height": 180
            },
            "high": {
              "url": "https://i.ytimg.com/vi/ZAxhEUfpSss/hqdefault.jpg",
              "width": 480,
              "height": 360
            }
          },
          "channelTitle": "jeffreestar",
          "liveBroadcastContent": "none",
          "publishTime": "2019-02-22T17:59:38Z"
        }
      }, {
        "kind": "youtube#searchResult",
        "etag": "a64y1aVRMk3NwQNbyagMA800Iw4",
        "id": {
          "kind": "youtube#video",
          "videoId": "AOkVEwMQOTM"
        },
        "snippet": {
          "publishedAt": "2020-07-14T19:00:06Z",
          "channelId": "UCucot-Zp428OwkyRm2I7v2Q",
          "title": "Prank Calling Makeup Stores! ft. Larray",
          "description": "HI SISTERS! In today's new video I prank called makeup stores like Morphe, Ulta, and Sephora to ask them what they thought about me and my palette.",
          "thumbnails": {
            "default": {
              "url": "https://i.ytimg.com/vi/AOkVEwMQOTM/default.jpg",
              "width": 120,
              "height": 90
            },
            "medium": {
              "url": "https://i.ytimg.com/vi/AOkVEwMQOTM/mqdefault.jpg",
              "width": 320,
              "height": 180
            },
            "high": {
              "url": "https://i.ytimg.com/vi/AOkVEwMQOTM/hqdefault.jpg",
              "width": 480,
              "height": 360
            }
          },
          "channelTitle": "James Charles",
          "liveBroadcastContent": "none",
          "publishTime": "2020-07-14T19:00:06Z"
        }
      }, {
        "kind": "youtube#searchResult",
        "etag": "3yatbTH84jt734-O-anjFtuVAgI",
        "id": {
          "kind": "youtube#video",
          "videoId": "5kI9fsf0S-c"
        },
        "snippet": {
          "publishedAt": "2019-07-19T18:00:09Z",
          "channelId": "UCucot-Zp428OwkyRm2I7v2Q",
          "title": "Letting The Person In Front of Me Decide My Makeup Routine",
          "description": "HI SISTERS! In today's video, I wanted to take on the Drive Thru challenge... but make it a Makeup Challenge! I went to Ulta and let The Person In Front Of Me ...",
          "thumbnails": {
            "default": {
              "url": "https://i.ytimg.com/vi/5kI9fsf0S-c/default.jpg",
              "width": 120,
              "height": 90
            },
            "medium": {
              "url": "https://i.ytimg.com/vi/5kI9fsf0S-c/mqdefault.jpg",
              "width": 320,
              "height": 180
            },
            "high": {
              "url": "https://i.ytimg.com/vi/5kI9fsf0S-c/hqdefault.jpg",
              "width": 480,
              "height": 360
            }
          },
          "channelTitle": "James Charles",
          "liveBroadcastContent": "none",
          "publishTime": "2019-07-19T18:00:09Z"
        }
      }]
    }
    videos_ids="gSa0e34EZyQ,YxoSmwXhvdw,ZAxhEUfpSss,AOkVEwMQOTM,5kI9fsf0S-c"

    self.assertEqual(get_videos_ids(search_response), videos_ids)

  def test_get_videos_data(self):

    search_response={
      "kind": "youtube#searchListResponse",
      "etag": "v6dM80l-6N7XAw0vC_a-ke30Yq4",
      "nextPageToken": "CAoQAA",
      "regionCode": "CO",
      "pageInfo": {
        "totalResults": 1000000,
        "resultsPerPage": 10
      },
      "items": [{
        "kind": "youtube#searchResult",
        "etag": "EMdBOdJXt9T87j1Sa-bnMKlCKuw",
        "id": {
          "kind": "youtube#video",
          "videoId": "gSa0e34EZyQ"
        },
        "snippet": {
          "publishedAt": "2019-06-16T06:30:05Z",
          "channelId": "UCt_KDu-DtBqvIw7X-V7mlmQ",
          "title": "Pari&#39;s Magical Beauty Parlour | Pari Doing Makeup | Funny Video",
          "description": "In today's Video i have opened a Beauty Parlour and i am doing very beautiful makeup of customers . So watch it and enjoy. Links to buy the products = 1. Magic ...",
          "thumbnails": {
            "default": {
              "url": "https://i.ytimg.com/vi/gSa0e34EZyQ/default.jpg",
              "width": 120,
              "height": 90
            },
            "medium": {
              "url": "https://i.ytimg.com/vi/gSa0e34EZyQ/mqdefault.jpg",
              "width": 320,
              "height": 180
            },
            "high": {
              "url": "https://i.ytimg.com/vi/gSa0e34EZyQ/hqdefault.jpg",
              "width": 480,
              "height": 360
            }
          },
          "channelTitle": "Pari's Lifestyle",
          "liveBroadcastContent": "none",
          "publishTime": "2019-06-16T06:30:05Z"
        }
      }, {
        "kind": "youtube#searchResult",
        "etag": "HwLipIMdNkx-iPl9AxDMSQf0zIo",
        "id": {
          "kind": "youtube#video",
          "videoId": "YxoSmwXhvdw"
        },
        "snippet": {
          "publishedAt": "2015-09-13T05:10:15Z",
          "channelId": "UCQ2WjcRRelz7iLn9s0igjww",
          "title": "Giant Surprise Egg 1 - Barbie, Monster High, Peppa Pig, and Play Doh - Toys R Us Shopping Spree",
          "description": "Giant Surprise Egg 1 is the first in a new series from Kaylee Bug Tv. Kaylee goes shopping for Barbie, Monster High, Peppa Pig, Play Doh, and more. All of these ...",
          "thumbnails": {
            "default": {
              "url": "https://i.ytimg.com/vi/YxoSmwXhvdw/default.jpg",
              "width": 120,
              "height": 90
            },
            "medium": {
              "url": "https://i.ytimg.com/vi/YxoSmwXhvdw/mqdefault.jpg",
              "width": 320,
              "height": 180
            },
            "high": {
              "url": "https://i.ytimg.com/vi/YxoSmwXhvdw/hqdefault.jpg",
              "width": 480,
              "height": 360
            }
          },
          "channelTitle": "Kaylee Bug Tv",
          "liveBroadcastContent": "none",
          "publishTime": "2015-09-13T05:10:15Z"
        }
      }, {
        "kind": "youtube#searchResult",
        "etag": "Cbh94n-zyeVW_Boc4F1AU7w4DEw",
        "id": {
          "kind": "youtube#video",
          "videoId": "ZAxhEUfpSss"
        },
        "snippet": {
          "publishedAt": "2019-02-22T17:59:38Z",
          "channelId": "UCkvK_5omS-42Ovgah8KRKtg",
          "title": "Trying TJ MAXX Makeup For The First Time",
          "description": "HEY EVERYONE... Welcome BACK to my channel! Today I go to TJ MAXX for the first time in 10 years and try to find a full face of makeup! Follow me on this ...",
          "thumbnails": {
            "default": {
              "url": "https://i.ytimg.com/vi/ZAxhEUfpSss/default.jpg",
              "width": 120,
              "height": 90
            },
            "medium": {
              "url": "https://i.ytimg.com/vi/ZAxhEUfpSss/mqdefault.jpg",
              "width": 320,
              "height": 180
            },
            "high": {
              "url": "https://i.ytimg.com/vi/ZAxhEUfpSss/hqdefault.jpg",
              "width": 480,
              "height": 360
            }
          },
          "channelTitle": "jeffreestar",
          "liveBroadcastContent": "none",
          "publishTime": "2019-02-22T17:59:38Z"
        }
      }, {
        "kind": "youtube#searchResult",
        "etag": "a64y1aVRMk3NwQNbyagMA800Iw4",
        "id": {
          "kind": "youtube#video",
          "videoId": "AOkVEwMQOTM"
        },
        "snippet": {
          "publishedAt": "2020-07-14T19:00:06Z",
          "channelId": "UCucot-Zp428OwkyRm2I7v2Q",
          "title": "Prank Calling Makeup Stores! ft. Larray",
          "description": "HI SISTERS! In today's new video I prank called makeup stores like Morphe, Ulta, and Sephora to ask them what they thought about me and my palette.",
          "thumbnails": {
            "default": {
              "url": "https://i.ytimg.com/vi/AOkVEwMQOTM/default.jpg",
              "width": 120,
              "height": 90
            },
            "medium": {
              "url": "https://i.ytimg.com/vi/AOkVEwMQOTM/mqdefault.jpg",
              "width": 320,
              "height": 180
            },
            "high": {
              "url": "https://i.ytimg.com/vi/AOkVEwMQOTM/hqdefault.jpg",
              "width": 480,
              "height": 360
            }
          },
          "channelTitle": "James Charles",
          "liveBroadcastContent": "none",
          "publishTime": "2020-07-14T19:00:06Z"
        }
      }, {
        "kind": "youtube#searchResult",
        "etag": "3yatbTH84jt734-O-anjFtuVAgI",
        "id": {
          "kind": "youtube#video",
          "videoId": "5kI9fsf0S-c"
        },
        "snippet": {
          "publishedAt": "2019-07-19T18:00:09Z",
          "channelId": "UCucot-Zp428OwkyRm2I7v2Q",
          "title": "Letting The Person In Front of Me Decide My Makeup Routine",
          "description": "HI SISTERS! In today's video, I wanted to take on the Drive Thru challenge... but make it a Makeup Challenge! I went to Ulta and let The Person In Front Of Me ...",
          "thumbnails": {
            "default": {
              "url": "https://i.ytimg.com/vi/5kI9fsf0S-c/default.jpg",
              "width": 120,
              "height": 90
            },
            "medium": {
              "url": "https://i.ytimg.com/vi/5kI9fsf0S-c/mqdefault.jpg",
              "width": 320,
              "height": 180
            },
            "high": {
              "url": "https://i.ytimg.com/vi/5kI9fsf0S-c/hqdefault.jpg",
              "width": 480,
              "height": 360
            }
          },
          "channelTitle": "James Charles",
          "liveBroadcastContent": "none",
          "publishTime": "2019-07-19T18:00:09Z"
        }
      }]
    }

    statistics_response={
      "kind": "youtube#videoListResponse",
      "etag": "oHg8KRrtlgo4dnpLD83JEtm8s8s",
      "items": [{
        "kind": "youtube#video",
        "etag": "bCuJZrDB-1gy5oV93m2Sif-YGwc",
        "id": "gSa0e34EZyQ",
        "statistics": {
          "viewCount": "49939877",
          "likeCount": "398582",
          "dislikeCount": "108330",
          "favoriteCount": "0"
        }
      }, {
        "kind": "youtube#video",
        "etag": "di7sIwEnxRMs4Fc3UIaoQk508gc",
        "id": "YxoSmwXhvdw",
        "statistics": {
          "viewCount": "49737287",
          "likeCount": "109520",
          "dislikeCount": "39387",
          "favoriteCount": "0"
        }
      }, {
        "kind": "youtube#video",
        "etag": "DXJo1P_U4LH4ijtS6XqY36goYuA",
        "id": "ZAxhEUfpSss",
        "statistics": {
          "viewCount": "23965302",
          "likeCount": "735926",
          "dislikeCount": "14970",
          "favoriteCount": "0",
          "commentCount": "614770"
        }
      }, {
        "kind": "youtube#video",
        "etag": "Bxm5JdsZ2Zf9DDebzNZeL8X1PwI",
        "id": "AOkVEwMQOTM",
        "statistics": {
          "viewCount": "8816624",
          "likeCount": "549713",
          "dislikeCount": "6418",
          "favoriteCount": "0",
          "commentCount": "26831"
        }
      }, {
        "kind": "youtube#video",
        "etag": "NZF68eutA4-jmmxAR7PTeYzhqlk",
        "id": "5kI9fsf0S-c",
        "statistics": {
          "viewCount": "8570335",
          "likeCount": "349157",
          "dislikeCount": "18317",
          "favoriteCount": "0",
          "commentCount": "75752"
        }
      }],
      "pageInfo": {
        "totalResults": 10,
        "resultsPerPage": 10
      }
    }

    videos_data=[{
      "id":"gSa0e34EZyQ",
      "title": "Pari's Magical Beauty Parlour | Pari Doing Makeup | Funny Video",
      "description": "In today's Video i have opened a Beauty Parlour and i am doing very beautiful makeup of customers . So watch it and enjoy. Links to buy the products = 1. Magic ...",
      "channel_title": "Pari's Lifestyle",
      "image_low_res": "https://i.ytimg.com/vi/gSa0e34EZyQ/mqdefault.jpg",
      "image_high_res": "https://i.ytimg.com/vi/gSa0e34EZyQ/hqdefault.jpg",
      "published_at": "2019-06-16T06:30:05Z",
      "view_count": "49939877"
    }, {
      "id":"YxoSmwXhvdw",
      "title": "Giant Surprise Egg 1 - Barbie, Monster High, Peppa Pig, and Play Doh - Toys R Us Shopping Spree",
      "description": "Giant Surprise Egg 1 is the first in a new series from Kaylee Bug Tv. Kaylee goes shopping for Barbie, Monster High, Peppa Pig, Play Doh, and more. All of these ...",
      "channel_title": "Kaylee Bug Tv",
      "image_low_res": "https://i.ytimg.com/vi/YxoSmwXhvdw/mqdefault.jpg",
      "image_high_res": "https://i.ytimg.com/vi/YxoSmwXhvdw/hqdefault.jpg",
      "published_at": "2015-09-13T05:10:15Z",
      "view_count": "49737287"
    }, {
      "id": "ZAxhEUfpSss",
      "title": "Trying TJ MAXX Makeup For The First Time",
      "description": "HEY EVERYONE... Welcome BACK to my channel! Today I go to TJ MAXX for the first time in 10 years and try to find a full face of makeup! Follow me on this ...",
      "channel_title": "jeffreestar",
      "image_low_res": "https://i.ytimg.com/vi/ZAxhEUfpSss/mqdefault.jpg",
      "image_high_res": "https://i.ytimg.com/vi/ZAxhEUfpSss/hqdefault.jpg",
      "published_at": "2019-02-22T17:59:38Z",
      "view_count": "23965302"
    }, {
      "id": "AOkVEwMQOTM",
      "title": "Prank Calling Makeup Stores! ft. Larray",
      "description": "HI SISTERS! In today's new video I prank called makeup stores like Morphe, Ulta, and Sephora to ask them what they thought about me and my palette.",
      "channel_title": "James Charles",
      "image_low_res": "https://i.ytimg.com/vi/AOkVEwMQOTM/mqdefault.jpg",
      "image_high_res": "https://i.ytimg.com/vi/AOkVEwMQOTM/hqdefault.jpg",
      "published_at": "2020-07-14T19:00:06Z",
      "view_count": "8816624"
    }, {
      "id": "5kI9fsf0S-c",
      "title": "Letting The Person In Front of Me Decide My Makeup Routine",
      "description": "HI SISTERS! In today's video, I wanted to take on the Drive Thru challenge... but make it a Makeup Challenge! I went to Ulta and let The Person In Front Of Me ...",
      "channel_title": "James Charles",
      "image_low_res": "https://i.ytimg.com/vi/5kI9fsf0S-c/mqdefault.jpg",
      "image_high_res": "https://i.ytimg.com/vi/5kI9fsf0S-c/hqdefault.jpg",
      "published_at": "2019-07-19T18:00:09Z",
      "view_count": "8570335"
    }]
    
    self.assertListEqual(get_videos_data(search_response,statistics_response),videos_data)

if __name__ == '__main__':
    unittest.main()

