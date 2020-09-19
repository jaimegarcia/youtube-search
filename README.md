## Youtube Powered Search

This tool allow the user to search videos related with a topic using Youtube Data API.

The DEMO is available in a link provided by email.


### Screenshots of the Tool in Desktop, Tablet and Mobile


**Search Input**
![alt text](https://github.com/jaimegarcia/youtube-search/blob/master/images/makrwatch-1.png?raw=true)


**Web Desktop**
![alt text](https://github.com/jaimegarcia/youtube-search/blob/master/images/makrwatch-2.png?raw=true)


**Web Tablet**
![alt text](https://github.com/jaimegarcia/youtube-search/blob/master/images/makrwatch-3.png?raw=true)


**Web Mobile**
![alt text](https://github.com/jaimegarcia/youtube-search/blob/master/images/makrwatch-4.png?raw=true)


### Architecture

The backend was made on Python using FastAPI and Google API Python Client. For unit testing in the backend I use Python UnitTest.

The Front End was built using React and Material UI. For unit testing I use React Testing Library with Jest.

The Server is composed by one main file and two helpers:

- For extracting videos ids from the Youtube search query 
- For exracting and merging the search query and video response with statistics, creating a list of videos

The front-end includes a search input and inifinite scroll loading till 200 videos. The design is responsive and change in mobile (similar design that the Youtube mobile app)

The communication between Back and Front is performed by using REST API through a GET Request


### Running in Local Environment
For running this project in your local environment you can use docker-compose


```bash
# Get the project
git clone https://github.com/jaimegarcia/youtube-search

# Enter to the directory
cd youtube-search

# Include your Youtube key in the key.py file in the server
api_key="YOUR_API_KEY"

# Build and Run server and web
docker-compose up --build
```

The web runs by default in http://localhost:3000
The server runs by default in http://localhost


You can also build the backend and frontend independently using the following commands:
```bash

# Build Server
docker-compose build youtube_server

# Build Web
docker-compose build youtube_web

#Run without building
docker-compose up
```

For running the tests, you can use docker-compose or python in the server, and docker-compose, npm or yarn in the web

Using docker-compose
```bash

#  Run Server Python UnitTest
docker-compose run youtube_server python -m unittest test

#  Run Web React Tests
docker-compose run youtube_web npm test

```
