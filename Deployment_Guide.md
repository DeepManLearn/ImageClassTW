# Deployment Guide

The App is deployed on [Heroku: Cloud Application Platform](https://www.heroku.com/) for continous integration, deployement and availability.

But due to Slug size limit of 500 MB on Heroku, the app was dockerized and deployed in Heroku container.
 
## Dockerization

To reduce the App image, the container is build using slim version of Python and CPU only version of Pytorch. ( See [Dockerfile](Dockerfile) )

Use following commands to build container and run on local machine:

```
docker build -t bird-img-classifier .
docker run -p 5000:5000 -it bird-img-classifier 
```

## Heroku Container Creation & Deployment

Create Heroku account on [www.heroku.com](https://www.heroku.com/). 

Login to Heroku from local machine using following command after dowloading and installing Heroku CLI.
  
```
heroku login
heroku container:login
```

Create container on Heroku, build and deploy the image :

```
heroku create bird-img-classifier

heroku container:push web --app bird-img-classifier

heroku container:release web --app bird-img-classifier
```

Following commands can be used to access the app from local browser and checking app logs:

```
heroku open --app bird-img-classifier
heroku logs --tail --app bird-img-classifier
```

Note:  After 15 minutes of inactivity, Heroku will suspend the app.  The next time the web app is called, Heroku will restart the app.  There could be a slight delay in starting the app.
 
## Twilio Sandbox Configuration

Configure Twilio sandbox by entering incoming message handler endpoint as App url on heroku https://bird-img-classifier.herokuapp.com/whatsapp

![Config](assets/SandboxConfig.PNG)

## Test the app
- The App can be tested by joining Twilio Sandbox by sending a ![Join](assets/SandboxJoin.PNG)
- After successfully joining send any message or Image.
- As explained above App may be restating on Heroku, so first message might get timedout. Please, try again afer 2-3 minutes. 
- Give it a try!  . 

