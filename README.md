# Serpent Tracker 
![Build and Test](https://github.com/serpent-tracker/serpent-tracker/workflows/Build%20and%20Test/badge.svg?branch=master)

The snake tracking solution based on Django and VueJS.  Will track snake husbandry information and will have an API and frontend.

# Local Setup

1. Create a `.env.dev` file based off `.env.dev.example`

```
mv .env.dev.example .env.dev
```

2. Modify the `.env.dev` file to your needs.

3. Build the Docker Compose setup:

```
docker-compose build
```


4. Bring up the services:

```
docker-compose up -d
```

5. Run the migrations for django:

```
docker-compose exec web python manage.py migrate --noinput
```

# Production Setup
More coming soon but for now the following will spin up nginx reverse proxy with django using wsgi with staticfiles in nginx as well.

```
docker-compose -f docker-compose.prod.yml up -d --build
docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear
```

# Shell Commands
Below are some commands you can run via the docker compose setup against the containers.

## Postgres Commands
You can get a shell to postgres via:

```
docker-compose exec db psql --username=serpenttracker --dbname=stracker
```

# Run Tests
You can run the test suite via:

```
source venv/bin/activate
cd serpenttracker
python manage.py test
```
