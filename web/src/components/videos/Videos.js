import React,{useState} from 'react';
import axios from 'axios';
import InfiniteScroll from 'react-infinite-scroller';

import Video from './Video'

function Videos() {
  
  const [videos, setVideos] = useState([{"id":"EzwZPAyb9Ns","title":"FIVE BELOW SHOPPING!!! *AFFORDABLE* MAKEUP!","description":"Come Shopping with me to FIVE BELOW For AFFORDABLE Makeup! ••••••••••••••••••••••••••••••••••••••••••••••••••• DISCOUNT CODES *GET A FREE MORPHE ...","channel_title":"Makeupbypita","image":"https://i.ytimg.com/vi/EzwZPAyb9Ns/mqdefault.jpg","published_at":"2019-03-11T00:23:33Z","view_count":"179364"},{"id":"rrX-3YA1tU0","title":"MAKEUP SHOPPING AT MORPHE AND SEPHORA! Shopping Vlog","description":"Today I went to the MORPHE makeup store for the very first time! It was so cool being able to see the products in person as opposed to online. Since I was at the ...","channel_title":"Lauren's Beauty","image":"https://i.ytimg.com/vi/rrX-3YA1tU0/mqdefault.jpg","published_at":"2019-05-26T23:19:52Z","view_count":"28779"},{"id":"sJmuGE-QdJc","title":"SHOP WITH ME .... makeup shopping video","description":"I went to ulta and did some shopping. Love shopping and specially for makeup. I got some new makeup for my trip and I'm so excited to show you guys!","channel_title":"Sophie Michelle","image":"https://i.ytimg.com/vi/sJmuGE-QdJc/mqdefault.jpg","published_at":"2018-11-09T19:10:20Z","view_count":"329018"},{"id":"842CO8OMSH8","title":"Makeup Shopping at Ulta","description":"Makeup Shopping at Ulta #makeup #shopping #ulta Check out our iPhone Videos; Smallest iPhone EVER Shopping Vlog https://youtu.be/u3YLEJbXvZ8 iPhone ...","channel_title":"Mommyof3xo","image":"https://i.ytimg.com/vi/842CO8OMSH8/mqdefault.jpg","published_at":"2019-08-02T23:23:51Z","view_count":"117198"},{"id":"Zuw1CNg83Lw","title":"MAKEUP SHOPPING VLOG WITH MY MOM | WHAT TO BUY FOR YOUR FIRST TEEN MAKEUP KIT!","description":"Don't forget to subscribe! https://bit.ly/WeissLifeSub In today's family vlog - Gabrielle & Mom go shopping for some makeup to make a first makeup starter kit for ...","channel_title":"THE WEISS LIFE","image":"https://i.ytimg.com/vi/Zuw1CNg83Lw/mqdefault.jpg","published_at":"2018-04-20T22:55:30Z","view_count":"2212080"},{"id":"EzwZPAyb9Ns","title":"FIVE BELOW SHOPPING!!! *AFFORDABLE* MAKEUP!","description":"Come Shopping with me to FIVE BELOW For AFFORDABLE Makeup! ••••••••••••••••••••••••••••••••••••••••••••••••••• DISCOUNT CODES *GET A FREE MORPHE ...","channel_title":"Makeupbypita","image":"https://i.ytimg.com/vi/EzwZPAyb9Ns/mqdefault.jpg","published_at":"2019-03-11T00:23:33Z","view_count":"179364"},{"id":"rrX-3YA1tU0","title":"MAKEUP SHOPPING AT MORPHE AND SEPHORA! Shopping Vlog","description":"Today I went to the MORPHE makeup store for the very first time! It was so cool being able to see the products in person as opposed to online. Since I was at the ...","channel_title":"Lauren's Beauty","image":"https://i.ytimg.com/vi/rrX-3YA1tU0/mqdefault.jpg","published_at":"2019-05-26T23:19:52Z","view_count":"28779"},{"id":"sJmuGE-QdJc","title":"SHOP WITH ME .... makeup shopping video","description":"I went to ulta and did some shopping. Love shopping and specially for makeup. I got some new makeup for my trip and I'm so excited to show you guys!","channel_title":"Sophie Michelle","image":"https://i.ytimg.com/vi/sJmuGE-QdJc/mqdefault.jpg","published_at":"2018-11-09T19:10:20Z","view_count":"329018"},{"id":"842CO8OMSH8","title":"Makeup Shopping at Ulta","description":"Makeup Shopping at Ulta #makeup #shopping #ulta Check out our iPhone Videos; Smallest iPhone EVER Shopping Vlog https://youtu.be/u3YLEJbXvZ8 iPhone ...","channel_title":"Mommyof3xo","image":"https://i.ytimg.com/vi/842CO8OMSH8/mqdefault.jpg","published_at":"2019-08-02T23:23:51Z","view_count":"117198"},{"id":"Zuw1CNg83Lw","title":"MAKEUP SHOPPING VLOG WITH MY MOM | WHAT TO BUY FOR YOUR FIRST TEEN MAKEUP KIT!","description":"Don't forget to subscribe! https://bit.ly/WeissLifeSub In today's family vlog - Gabrielle & Mom go shopping for some makeup to make a first makeup starter kit for ...","channel_title":"THE WEISS LIFE","image":"https://i.ytimg.com/vi/Zuw1CNg83Lw/mqdefault.jpg","published_at":"2018-04-20T22:55:30Z","view_count":"2212080"}]);
  
  return (
    <div>
      <InfiniteScroll
        pageStart={0}>
        <div className="tracks">
            {videos.map((video)=><Video key={video.id} video={video}/>)}
        </div>
      </InfiniteScroll>
    </div>
  );
}

export default Videos;
