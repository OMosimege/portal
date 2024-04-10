**Employer Web Portal**

About the project:

Proof of Concept (PoC) of an API, a solution built in django, for scheduler (cron job) that runs every 5 minutes to check whether any announcements need to be sent

## Requirements

- Docker
- Docker-compose
- Makefile reader installed on device

## Installations guide

### Using Docker-compose

1. docker-compose up --build
2. docker-compose down

### Using Makefile

1. Clone the repository
2. Run `make build` to build the docker image
3. Run `make run` to run the docker container
4. Run `make stop` to stop the docker container
5. Run `make test` to run the unit tests
6. Run `make up` to have the app up and running



### Documentation
See file in folder `docs` in main repository





