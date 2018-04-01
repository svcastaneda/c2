# CoderDojoChi v2

## Requirements
- Docker

## Installation
1. Fork this repo.
2. Run the following commands changing `USERNAME` to your GitHub username.

```bash
git clone git@github.com:USERNAME/c2.git && cd c2
git remote add upstream git@github.com:CoderDojoChi/c2.git
docker-compose up
```

## Running the App

```bash
# Running with log output
docker-compose up

# Running daemon mode (in the background)
docker-compose up -d

# Attaching a log output to already-running process
docker-compose logs nginx
docker-compose logs web
docker-compose logs db
```

---

## Management
For a full list of management options, start the app, then create a shell into the instance. the following commands:
```bash
# In one window
docker-compose up

# In another window
docker-compose run web bash
invoke --list
```

## Migrations
```bash
# Create migrations
docker-compose run web python manage.py makemigrations

# Run Migrations
docker-compose run web python manage.py migrate
```

---

## Testing
```bash
# Run all tests
docker-compose run web invoke django-test

# Run test for <app>
docker-compose run web invoke django-test <app>

# Example for 'account' app
docker-compose run web invoke django-test account
```

---

## Deployment
```bash
```
