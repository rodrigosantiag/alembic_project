# Alembic Project

#### Requirements

- Make
- Python 3.11
- Docker
- Docker Compose
- Pip
- Other requirements:
    - requirements.txt
    - requirements-dev.txt (development dependencies)

#### Installing dev environment requirements:

```shell
make install-dev
```

#### Linting and formatting code:

```shell
make lint
make format
```

#### Build application:

```shell
make build
```

#### Run application:

```shell
make up
```

#### Build and then run application
```shell
make build-up
```

#### Stop application

```shell
make down
```

#### Restart application

```shell
make restart
```

#### Restart building application

```shell
make build-restart
```

#### Check application logs:

```shell
make logs
```

## Description

It's a very simple project to prove a concept that it's possible to manage several databases through a single alembic project (this project must not be a base for anything that will be in production someday).

To generate and run migrations, the following commands must run in the virtual environment created by `make install-dev` command.

Generate migration:

```shell
alembic -n <database name> revision -m "Migration title"
```

Run pendent migrations:

```shell
export $(cat .env | xargs) && alembic -n <database name> upgrade head
```

The `export` command above is necessary if you run the command outside of the container. Otherwise, you can start the `service` container and run the following command:

```shell
alembic -n <database name> upgrade head
```

## Available databases

The following database are available by default in the project:

```text
postgres_database
disbursement_database
mysql_database
```
