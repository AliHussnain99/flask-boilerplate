<br/>
<p align="center">
  <h3 align="center">Flask Boilerplate</h3>

  <p align="center">
    Flask is often used to quickly build APIs because it's simple. But when projects get bigger, it can become tricky to handle. I've made a starting point (boilerplate) that organizes the code in a way that's easy to understand and scalable, similar to Django. This makes it simpler to manage larger projects as they grow.
    <br/>
  </p>
</p>

## Table Of Contents

* [About the Project](#about-the-project)
* [Built With](#built-with)
* [Getting Started](#getting-started)
    * [Prerequisites](#prerequisites)
    * [Installation](#installation)
* [Authors](#authors)

## About The Project

Lately, I've been engaged in various projects involving the use of Flask for API development. While I have a fondness
for the organized structure that Django offers, my recent experiences with Flask have presented a different narrative.
As a result, I've decided to create a boilerplate that encompasses essential features for web development. Here are the
key components.

* Setting up Dockerization
* Incorporating Celery for distributed asynchronous tasks
* Integrating Celery Beat for scheduling asynchronous tasks
* Implementing SQL Alchemy and Alembic for ORM (Object-Relational Mapping) and migrations
* Completing the setup for environment variables and logging
* Integrating PostgreSQL as the database
* Defining a middleware structure, with a sample middleware * demonstrating a maintenance page based on the environment
  value
* Establishing an application structure inspired by Django
* Swagger is integrated for API docs

## Built With

* Python
* Flask
* Docker

## Getting Started

Here are the minimum and absolute steps to run this boilerplate on your local environment

### Prerequisites

You should have docker installed on your machine. Please visit the docker official site(https://www.docker.com) to
download docker for your machine-compatible OS.

### Installation

1. Set env values according to environment(local,development,production).For setting env, go to the core application,
   open the env folder, and set values according to your environment. A sample file is placed in each environment
   folder.

2. Build the image by

```shell
docker-compose build
```

3. Run the build by

```sh
docker-compose up
```

4. Yay! Now you can access http://localhost:5000/
5. You can find all project related settings in `core/settings.py`.This file has proper comments so that you can know how to register models,views,middlewares stuff.
## Authors

* [Ali Hussnain](https://github.com/AliHussnain99)
