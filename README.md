# Minesweeper Backend

# Stack used:

-   [Python 3.8][stack/python]
-   [Django 3.1.3][stack/django]
-   [Django Rest Framework][stack/drf]
-   [MySQL 8][stack/mysql]
-   [Black][stack/black] and [Flake8][stack/flake8] for codestyling
-   [APICURIO, for API documentation][stack/apicurio]
-   [Docker][stack/docker]

OpenAPI 3 documentation: [https://apidoc.mines.makecodes.dev/][url/apidoc]
Game frontend: [https://mines.makecodes.dev/][url/the-game]
Frontend github repo: [https://github.com/imakecodes/minesweeper-frontend][github/frontend]

### Production environment

Was used [Digital Ocean][stack/do] to host the applications using a little droplet with 1GB/25GB with Ubuntu 20.04 LTS at New York with Docker and Nginx(for reverse proxy).

Also was used Github Actions to create docker images for [backend][github/image-backend] and [frontend][github/image-frontend]

# Next desired steps

-   Change the primary key of the game from Integer to UUID to avoid cheating from the players
-   User authentication to store the match history
-   Create a global and by user scoreboard
-   Create unit tests

# Running locally

Assuming you have docker-compose and docker installed on your computer:

### Clone the repository

```bash
git clone git@github.com:imakecodes/minesweeper-backend.git
cd minesweeper-backend
```

### Run the application

```bash
docker-compose up -d
```

### Run the migrations

```bash
docker-compose run app python manage.py migrate
```

The application will be available at [http://localhost:8000](http://localhost:8000)

[stack/python]: https://www.python.org/
[stack/do]: https://www.digitalocean.com/
[stack/django]: https://www.djangoproject.com/
[stack/drf]: https://www.django-rest-framework.org/
[stack/mysql]: https://www.mysql.com/
[stack/black]: https://github.com/psf/black
[stack/flake8]: https://flake8.pycqa.org/en/latest/
[stack/docker]: https://www.docker.com/
[stack/apicurio]: https://www.apicur.io/
[github/frontend]: https://github.com/imakecodes/minesweeper-frontend
[url/apidoc]: https://apidoc.mines.makecodes.dev/
[url/the-game]: https://mines.makecodes.dev/
[github/image-backend]: https://github.com/imakecodes/minesweeper-backend/packages/493329
[github/image-frontend]: https://github.com/imakecodes/minesweeper-frontend/packages/493379
