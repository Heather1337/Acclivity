## Acclivity 

Created by: Heather Piverotto, Angela Purcell, Bekah McCurry, Jiyoung Yoon
**************************************************************************************************
  
UI allows users to view dividend stocks (1,000 data points sourced from two APIs) by sector
**************************************************************************************************
![UI for Acclivity](https://media.giphy.com/media/edepEkos9upI3Ig0za/giphy.gif)


User has the ability to view real time updates when adding/removing dividends from their portfolio
**************************************************************************************************
![Real time updates for Dashboard](https://media.giphy.com/media/7ukWQEDmqEInCbPlOR/giphy.gif)


## Inspiration
Acclivity is a physical upward slope; the same visual an investor would ideally see in their investment portfolio.
The market activity of the last two months made us acutely aware that investing could be made more accessible to individuals without a finance background. We're presenting a more simple approach to stock investing by highlighting dividend distributing stocks.


## What it does
Acclivity allows users to build a mock dividend portfolio based on a concise presentation of the risk, industry diversification, and cost/payout.


## How we built it
While researching the API endpoint options, we determined our basic wireframe and database schema, then used that structure to create our table relationships. After retrieving data from multiple polygon.io endpoints, we parsed through the responses to build up our stock data. We seeded the stocks table in our database using our scraped data and established the CRUD operations to begin implementing user functionality. There, we added stock routes, user stock routes, user dashboard routes, and login routes, to be called in our server file. Our server routes and corresponding react components were next,
## Challenges we ran into
Our biggest challenge by far was sourcing and mining data. While there are quite a few financial APIs we considered, the data we needed was not located in a single endpoint, instead, we had to utilize three separate endpoints from polygon.io, and parse data from each response object. The API we used had a pretty low limit of API calls per minute, so it required us to establish a lengthy function breakdown to swap out API keys, as we mined over 1000 stocks in order to get a broad enough representation.


## Accomplishments that we're proud of
Competing in our first hackathon!
Successfully parsing through our API response objects and csvs to seed our database using DRY functions.
Developing such a clean presentation of dividend stock options.
Creating an effective stock increment/decrement for client profiles.


## What we learned
Git is a necessary evil.
Dynamic graphs are not something we can learn in an hour.

## What's next for Acclivity
We'd like to integrate part of our inspiration - twitter posts - to track stocks and companies receiving buzz. Imagine setting up your stock profile to receive alerts if Elon Musk tweets something about a company.
What financial app is complete without a graph? Employing a dynamic graph that changes with user input would add a welcome visual element of usefulness and user-ease. This could present a visual representation of the user stock dashboard from the top of the page - ie, expected dividend amount/payout, or portfolio diversification.

