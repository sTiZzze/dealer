# Dealership

## Description

The logic of the project is divided into 3 main parts, a car dealership, car suppliers, and a buyer. The car dealership buys cars from the supplier, then the car is sent to the buyer from the car dealership. All possible discounts at each of the sublevels are taken into account.

## How to run

Create virtual env:

```
python -m venv .venv
```
Configure environment variables:

```
cp .env.sample .env
```

Start services

```
docker-compose up -d postgres redis
```

Apply migrations

```
docker-compose run app python manage.py migrate
```

Start app

```
docker-compose up app
```

## How to run locally
Activate virtual env:

```
. .venv/Scripts/activate
```

Install dependencies:

```
pip install -r requirements.txt
```

Start services:

```
docker-compose up -d
```

Run migrations

```
python manage.py migrate
```

Create super user:

```
python manage.py createsuperuser
```

Run server:

```
python manage.py runserver
```

## Urls

Access to admin: http://localhost:8000/admin/

Access to api: http://localhost:8000/api/

### Auth

Create access token: http://localhost:8000/api/token/

Refresh access token: http://localhost:8000/api/token/refresh/

### Posts

Manage issues: http://localhost:8000/api/posts/

### Create posts

Download image: http://localhost:8000/api/image/

## Run linter

```
make lint
```
