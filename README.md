# Basketball Game Generator


## Table of Contents

1. [Introduction](https://github.com/umayr12/SFIA2#Introduction)
    + [Requirements](https://github.com/umayr12/SFIA2#requirements)
2. [Project Plan](https://github.com/umayr12/SFIA2#project-plan)
3. [Building of the app](https://github.com/umayr12/SFIA2#Building-of-the-app)
    + [Errors](https://github.com/umayr12/SFIA2#Errors)
    + [During Build](https://github.com/umayr12/SFIA2#During-Build)
    + [End of Build](https://github.com/umayr12/SFIA2End-of-Build)
5. 


## Introduction
### Requirements
The requirements of the project are as follows:
+ An Asana board (or equivalent Kanban board tech) with full expansion on tasks needed to complete the project. This could also provide a record of any issues or risks that you faced creating your project.
+ An Application fully integrated using the Feature-Branch model into a Version Control System which will subsequently be built through a CI server and deployed to a cloud-based virtual machine.
+ If a change is made to a code base, then Webhooks should be used so that Jenkins recreates and redeploys the changed application
+ The project must follow the Service-oriented architecture that has been asked for.
+ The project must be deployed using containerisation and an orchestration tool.
+ As part of the project, you need to create an Ansible Playbook that will provision the environment that your application needs to run.
+ The project must make use of a reverse proxy to make your application accessible to the user.

## Project Plan

![image](https://user-images.githubusercontent.com/84901993/126125505-be170ffa-3beb-4f33-9a00-f0f4906e7ed8.png)
My Plan for this project was to have a CI Pipeline like the one displayed above. I intended to have my application running inside a Docker-Swarm,with nginx as a reverse proxy, built by Ansible. I then intended for this to be run via Jenkins, with Jenkins having a Webhook connection to Github so that any time code is pushed to Github, Jenkins will run the job with the new code implemented.

My plan for the application was to create a Basketball Games Generator.
+ Service 2 would be used to randomly select two Teams from a list to play each other
+ Service 3 would be used to randomly select a Stadium from a list
+ Service 4 would be used to retrieve the output from Service 2 and Service 3, and then use that information to return a % chance of one team winning over the other

## Building of the app
### Errors
During the building of the app I experienced a severe error that affected my whole project. My VM had become unaccessable and due to bad project management, I had not committed any of my code, which meant I had to start again from the beginning.

Error message:
![image](https://user-images.githubusercontent.com/84901993/126126398-eb7e2d06-2de7-4155-acf4-dfdb7527a280.png)

Due to time constraints relating to the error, I had no choice but to change my endgoal and aim to build my app so that it was deployable via Docker-Compose.

### During Build

![image](https://user-images.githubusercontent.com/84901993/126129689-2013d206-c200-4a36-97ac-c8e37704b3b5.png)
As seen above, my plan was to use Docker-Compose to build an app that utilised multiple containers with a different service in each. I also ensured my database was connected to the server, so that the server could give and recieve data to the database.With the server connected to all other services, I then planned to connect this server to NGINX, so that the user is interacting with the whole application via NGINX.

![image](https://user-images.githubusercontent.com/84901993/126130003-66de1615-ff5f-446b-9d1c-757e7f3c9b41.png)

### End of Build
![image](https://user-images.githubusercontent.com/84901993/126126622-2bc51906-e5c6-4b7f-8d53-7e2fd7618676.png)
At the end of the build my pipeline ended up looking like this, which is what I had planned for with the time constraints that I was under. 

![image](https://user-images.githubusercontent.com/84901993/126126665-ff3ef016-62b9-400b-ba0f-94d826e2ece0.png)

https://trello.com/b/mOHZJECA/project-2-board
