# Flask App with Redis - README

This repository contains a simple Flask application that integrates with Redis. The app simulates rolling a die and stores the roll history in Redis. Whilst ensuring persistence between runs with docker volumes (using redis).

## Prerequisites

Before you begin, ensure you have the following installed:

* [Docker](https://www.docker.com/products/docker-desktop) (for containerization)
* [Docker Compose](https://docs.docker.com/compose/) (for managing multi-container Docker applications)
* A modern browser (to access the web application)

## Getting Started
Follow these steps to get the application running on your local machine.

### 1. Clone the Repository
Start by cloning this repository to your local machine:

```bash
git clone https://github.com/noamseifer/MidTermDevops.git 
cd MidTermDevops
```

### 2. Build the Docker Containers

The project uses Docker to build the application image. Docker Compose is used to run both the web (Flask) service and the Redis service.

To build the containers:

```bash
docker-compose build
```

### 3. Start the Application

Once the build is complete, run the following command to start the application:

```bash
docker-compose up
```

This will start both the **Flask web service** and the **Redis service**. The Flask app will be available on your local machine.

### 4. Access the App

Open your browser and go to:

```
http://localhost:8000
```

This will load the main page of the application, where you can roll a die and view the roll history.

### 5. Stop the Application

To stop the running containers, press `CTRL+C` in the terminal where `docker-compose up` is running. You can also stop the containers in the background with:

```bash
docker-compose down
```

---

## Application endpoints:

1. **Roll a Die**: Navigate to `/roll` to simulate rolling a die. The roll will be recorded in the Redis database.
2. **View History**: Navigate to `/history` to see the history of all rolls.


### Docker Compose Setup

* **Flask App (`web` service)**: The Flask app runs on port `5000` inside the container. It's mapped to port `8000` on the host machine for access.
* **Redis (`redis` service)**: Redis runs on the default port `6379`. The Flask app connects to Redis by the service name `redis`, which Docker Compose automatically manages.


### Customizing the Port

If you want to change the port, you can modify the `FLASK_PORT` environment variable in the `docker-compose.yaml` file or by editing the `docker-compose.override.yaml`.

To change the port dynamically, set the environment variable like this:

```yaml
web:
  environment:
    - FLASK_PORT=5001
```
