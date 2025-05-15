# Guardian Vision

<p> <img src="https://user-images.githubusercontent.com/124444723/233845771-bd346166-71c1-4213-a015-9ce94515c755.jpg" alt="Guardian Vision Logo" width="100px" height="100px" style="background: #fff;"> </p>

<p> Violence detection ML model to detect suspicious activities in real-time through CCTV or any camera, and send immediate alert to the respective authorities. </p>

 <img src="static\images\WhatsApp Image 2023-04-24 at 01.06.23.jpg" width="900px" height="500p">

## Overview 🤖

The project aims to develop a system for violence detection using CCTV footage and providing an immediate alert to the police. The system will use advanced image processing and machine learning techniques to analyze the CCTV footage in real-time and detect any violent behavior or actions. Once detected, an automatic alert will be sent to the police, enabling them to respond quickly and take appropriate action. The system has the potential to enhance public safety and reduce crime rates in public areas.

## Usage

To use this project, you need to have a webcam connected to your computer. The project will capture the video stream from the webcam and analyze it for any violent activities. If any violence is detected, the project will send an alert to the respective authorities with the location and timestamp of the incident.

## Features 🦾

- Weapon Detection
- Light/dark mode toggle
- Enhance the user experience creating highly reactive website.

## Flow of the Project 💻

<li>  Home Page</li>  
 <p>This page help new user to understand our facilities and how our guardian vision works.It provides offer and This deviate user to our 
 user login page.</p>

<li>  Create Account</li>  
<p> Helps us to create account  in our platform.</p>

<li>  User Login</li>  
<p>The user log in to the platform using their registered email and password.</p>

<li>  User Interface</li>  
<p>The logged in user ca use our services of using his Webcam for Real-time AI detection of physical violence or can upload a video where the AI detects if there is any physical violence present in it.</p>

<li>  Webcam Page</li>  
<p>The User can give the email of his friends and family. Once the webcam start if any voilence detected ,it sends alert to all respective authorities along with the given emails by the User.</p>

<li>  Video upload Page</li>  
<p>The User can upload any video in our website after which the AI detects if there is any violence in it. If there is any suspicious activity present in it, the AI sends a image of that particular frame.</p>

## Tech Stack 🧑🏻‍💻

**Client:** <li>HTML</li>  
 <li>CSS</li>  
 <li>JAVASCRIPT</li>  
 <li>Bootstrap</li>

**Server:** <li> JSON</li>  
 <li> Node</li>

**Mchine Learning** <li> Python </li>
<li> Flask </li>  
 <li> Yolo Models </li>

## Installation

Install required packages for JSON server with npm \*Path should be the directory where Project is present

```bash
  npm i
  npm init -y
  npm install -g json-server
```

To Run the json-server on port 8000

```bash
  json-server --watch ./database/db.json --port 8000
```

Install the Basic libaray

```bash
   pip install flask
   pip install flask_wtf
   pip install twilio
   pip install smtplib
   pip install opencv-python opencv-python-headless
   pip install cv2
   pip install ultralytics
```

## Advantage of Guardian Vision

#Challenges in Real-world
1.Finding Database for ML model
2.Deployment of ML model on website.
3.Sending alert by sms and Emails.

#Solution
1.Creating/Finding and framming of database.
2.Deployment of ML model using Flask libaray.
3.Sending alert through Python libaray .

## Support

For support, email vigilantsquads@gmail.com

## Team Members 🧑‍🤝‍🧑

- [@maskboyAvi](https://github.com/maskboyAvi)
- [@aks](https://github.com/atharvsawant2003)
- [@CSNPSR](https://github.com/PavanaSakethaRam)
- [@GamezMartian](https://github.com/ydvmudit07)
- [@ayush_lion](https://github.com/Ayushlion8)

 <img src="static\images\WhatsApp Image 2023-04-24 at 01.07.02.jpg" width="900px" height="500p">

## Feedback

You can reach out to us at vigilantsquads@gmail.com where you can give feedbacks or report bugs.
