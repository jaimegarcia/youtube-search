## Youtube Powered Search

DEMO available in link provide it by email


![alt text](https://github.com/jaimegarcia/youtube-search/blob/master/images/makrwatch-1.png?raw=true)

![alt text](https://github.com/jaimegarcia/youtube-search/blob/master/images/makrwatch-2.png?raw=true)

![alt text](https://github.com/jaimegarcia/youtube-search/blob/master/images/makrwatch-3.png?raw=true)

![alt text](https://github.com/jaimegarcia/youtube-search/blob/master/images/makrwatch-4.png?raw=true)

The Front End was built using React and Material UI. For testing I use React Testing Library with Jest.

The Server is composed by one main file and helpers. The extracting of the videos ids from the Youtube search query 


For testing in the backend I use Python UnitTest

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


For running the tests, you can use docker-compose or python in the server, and docker-compose, npm or yarn in the web
```bash
# Go to the server folder
cd server

#  Run Python UnitTest
docker-compose run youtube_server python -m unittest test

# Go to the web folder
cd web
#  Run YARN Test
yarn test
```
