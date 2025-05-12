## Containerization & Docker

### Reading

- https://docs.docker.com/get-started/
- https://blog.logrocket.com/dockerizing-django-app/#creating-the-docker-files-and-docker-cli
- https://github.com/brendenwest/ad420/blob/main/6_containers.pdf
- https://hub.docker.com

### Practice 
- https://app.datacamp.com/learn/courses/introduction-to-docker

### Learning Outcomes

- Containerization
- Intro to Docker
- Dockerizing a Python app

### Containerization

Containerization is a technique for running applications in a self-contained `virtual` environment isolated from the underlying host operating system. 

Containerization allows an application to run in the same `virtual` environment on all developer machines and in development, test, and production environments. This minimizes potential problems such as:
- environments having different configurations,
- underlying dependencies changing without notice,

### Intro to Docker

Docker has become the most widely used 
app virtualization technology and is an essential skill for professional software developers.

Docker allows developers to define a static `image` (template) with OS and other environment configurations required for an application.

Developers can create one or more `containers` based on and image to run their application. Containers can run on a local computer for application development, or in a remote (e.g. cloud) environment for testing or production.

The Docker application has several components:
- **server** - a host that runs the Docker containerization engine (daemon)
- **daemon** - service that mediates interaction with containers on a host system
- **client** - applications such as a command-line interface (CLI) that enable interaction with a Docker server to manage containers

Docker (the company) also hosts a registry of pre-built `official` and community images that developers can use as a starting point for their images.

### Docker CLI

The Docker CLI allows one to manage docker images and containers via a command line interface (e.g. via Terminal or PowerShell).

Typical command structure is:

`docker <COMMAND> <OPTIONS>`

A few common commands are: 

- **build** - builds a container from a specified image
- **compose** - run multi-container applications specified in a `docker-composer.yml` file
- **exec** - executes a command in a running container
- **run** - runs a command in the specified container

[Docker CLI](https://docs.docker.com/reference/cli/docker/)

### Python requirements.txt files

`requirements.txt` is a file listing packages or libraries needed by a Python application that `pip` can read to install dependencies.

The file lists each `dependency` and a `version specifier` that can be exact or a logical rule. For example:

```commandline
Flask == 3.1.0
Flask-SQLAlchemy >= 3.0.0
```

It's not necessary to list every package that might get installed, since some packages may specify their own dependencies. But it's common to list all dependencies to prevent unplanned changes. 

For example, installing Flask will also install `Jinja2`, but you might want to enforce a specific version like this:

```commandline
Flask == 3.1.0
Jinja2 == 3.1.6
Flask-SQLAlchemy >= 3.0.0
```

See the full set of [requirements specifiers here](https://pip.pypa.io/en/stable/reference/requirement-specifiers/)

### Dockerizing a Python app

Docker images are defined in a `Dockerfile` that specifies a `base` image (operating system and configurations) and any application-specific modifications. For example:

```commandline
FROM python:3.12-slim
COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt
WORKDIR /app
ENTRYPOINT ["python"]
CMD ["app.py"]
```

The above commands:
- pulls an official Python 3.12 base image
- copies a requirements.txt file into the image
- installs python dependencies specified in requirements.txt into the image
- defines a command to run when a container is created from the image

See all [official Python images](https://hub.docker.com/_/python)

Docker containers can be started with the `docker run` command, but it's often easier to managing container configurations with a `docker-compose.yml` file. This declarative approach allows developers to specify run-time settings such as 
- mapping host-computer ports to container ports
- mapping host directories (volumes) to container directories
- setting environment variables
- defining other containers this application depends on 

For example, docker-compose.yml for a basic flask application might look like this:

```commandline
version: '3'
services:
  flask:
    image: flask_app
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - 3000:5000
    volumes:
      - "$PWD/app/:/app"
```
