## Youtube Powered Search

DEMO available in link provide it by email

Torre Mentors allows people to get their dream jobs, by providing job searching and mentoring access

This products focus on monetization. It considers two flows: 

1. Referral Aggregation: Provider give money by referral
2. Mentoring Fee: Mentor is charged a comission for every bussines. Alternative the fee can be charged to the end users

The user enters a query composed by Skills (Jobs with any of the skills) and Organizations  (Jobs from any of the orgs) 

![alt text](https://github.com/jaimegarcia/torre-plus-jobs/blob/master/images/search.png?raw=true)

![alt text](https://github.com/jaimegarcia/torre-plus-jobs/blob/master/images/search-light.png?raw=true)
To improve UX in the Opportunities view, I am querien on sizes of 50, and showing 10 by 10. The new 50 are saved in Redux Store,
so if the user goes back it doesn't need to query again the information. I'm also using Skeletons to improve Speed Perceptions.

![alt text](https://github.com/jaimegarcia/torre-plus-jobs/blob/master/images/pagination.png?raw=true)

Then, the user can check details about the Opportunity and see a shuffle of Mentors, which can help her/him to apply to the job.
After selecting the mentor a Credit Card form is display with the rate in the mentor currency, allowing to pay for mentorship.

![alt text](https://github.com/jaimegarcia/torre-plus-jobs/blob/master/images/detail.png?raw=true)


![alt text](https://github.com/jaimegarcia/torre-plus-jobs/blob/master/images/card.png?raw=true)


The database of users and payments remains on Stripe, I add metadata to match with the username of the mentor. 

![alt text](https://github.com/jaimegarcia/torre-plus-jobs/blob/master/images/stripe.png?raw=true)

The Front End was built using React and Material UI. For testing I use React Testing Library with Jest.

The Server is composed by one main file and helpers. The extracting of the videos ids from the Youtube search query 



The microservices are located together but are easy to separate thanks to its struture.

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
