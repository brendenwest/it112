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