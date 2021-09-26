# course2career
We offer both an _**API**_ and a _**website user interface**_ that allows developers and users to input Cornell courses and get job listings that build from the skills learned in those courses. This project was created for Big Red Hacks Hackathon 2021.

## As of September 2021:
The API could be found at [https://course2careerapi.herokuapp.com/](https://course2careerapi.herokuapp.com/) and  
the website could be accessed at [https://c2cc2c.course2career.tech/](https://c2cc2c.course2career.tech/).

# API Usage
The API offers 4 GET commands:
1. Get our course database:  
`https://course2careerapi.herokuapp.com/api/courses/`
2. Get a single course:  
`https://course2careerapi.herokuapp.com/api/courses/<subject>/<course_id>/`
3. Get Jobs matching keywords:  
`https://course2careerapi.herokuapp.com/api/jobs/<location>/<[keywords]>/`
4. Get Jobs matching a single course:  
`https://course2careerapi.herokuapp.com/api/jobs/<location>/<subject>/<course_id>/`

# Project Story
## Inspiration
University courses can spark new careers but are also huge investments of time and money. Especially for individuals who don't have a college degree, taking courses at a local university or community college can offer valuable skillsets and qualify them for higher-paying and more satisfying jobs. After taking a course, it can be hard to convert knowledge to real-world gains and take the next step in one’s career. Our hack responds to this need to evaluate the career benefit of courses and find opportunities that match the courses a student has taken.

## What it does
We offer both an _**API**_ and a _**website user interface**_ that allows developers and users to input Cornell courses and get job listings that build from the skills learned in those courses. This application can be _**used for evaluating courses or discovering opportunities**_ and is intended for both current students and individuals in the community considering Cornell courses. Through our API, we also offer access to our cleaned Cornell course database which includes extracted keywords from each course title and description.

## How we built it
### Backend
The core of our app is offering course and job offering data in meaningful ways to our clients. To build the course database, we _**processed courses from the Cornell course roster API**_ from Fall 2019 to Winter 2021. We formatted this data into a single database we could offer through our API. To facilitate job search, we _**extracted keywords from courses titles and descriptions**_ using the YAKE Python library. _**To collect relevant job opportunity data, we used Careerjet’s public search API**_. Careerjet API calls are done through their Python client on our Heroku hosted API. 

### API
Inle and Jan-Paul programmed the API in Python with Flask and hosted the API on Heroku using a domain.com domain name! _**The API offers 4 GET methods**_: get the course database, get a single course's info, get job listings matching keywords, and get a job listing matching the keywords of a specific course! We hosted our API on Heroku. 

### Frontend
Our website was designed in Figma and developed with HTML, JavaScript, and CSS. We have three main pages: a home page, a page for users to enter, read about, and select courses, and a page to display the job listings we found. Calls to the API are done with JavaScript. We hosted our website on Github pages

### Design
Together, we brainstormed our frontend design on notepads before drafting our UI design with Figma. _**Ibrahim created pixel-perfect mockups of webpages and components with Figma**_ that allowed us to showcase future features and code the website with a vision. 

## Challenges we ran into
We searched for a long time to find either a good API or a database of job listings. Jan-Paul was hard at work testing out and signing up for various APIs at Indeed, Glass Door, etc. before we finally found the CareerJet public API which fit exactly what we needed!

## Accomplishments that we're proud of
We’re proud of creating a working product in a single weekend! The features we are most proud of completing are the keyword extraction for the course database, the REST API (Inle’s first API!), and Ibrahim’s beautiful Figma designs.

## What we learned
This was our first Hackathon and we learned a ton! _**Figma was huge in planning and developing our frontend**_ and the Hackathon’s Design Workshop taught us a bunch of great shortcuts. It was also super fun working with new tools like keyword extraction with YAKE and the Careerjet API.

## What's next for Course2Career
We would love to offer Course2Career API and UI for other universities! For this project, we preprocessed a Cornell course database. However, the same UI, API structure, and keyword extraction functions could be used on courses from other universities too. We would especially be interested in serving community colleges and state universities. These colleges offer courses with valuable skills to people in the community at low prices.

We had several features we were interested in but knew we wouldn’t have time for. This included offering information on related courses, prerequisites, and login features. Figma was great at showcasing these future features! In the future, it would be awesome to add them to our app.
