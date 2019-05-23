# DistanceServer

This is the repo that holds the server for rpi-communication

# Installation
- This is made for running on a Heroku instance.

# Running Locally
- Install dependencies: `sudo pip install -r requirements.txt`
- Run: python3 app.y

# Design
- general
  - /api/... holds the API
  - /... holds the website
- Use with RaspberryPi
  - Hook RaspberryPi up and let it go to website. RPi will send
  key to register device to database so that you can register it.
  - On the website  
    1. Find your pi, with key
    2. Set settings
  - You are finished.

# TODO / Future things to fix
- Add Swagger / OpenAPI documentation to the API
- Make site look better
- Finish implementing registration
