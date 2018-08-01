# CoderDojoChi v2

## Requirements
- Docker

---

## Installation
1. Fork this repo.
2. Run the following commands changing `USERNAME` to your GitHub username.

```bash
# Clone forked repo
git clone git@github.com:USERNAME/c2.git

# Go into project repository
cd c2

# Add upstream remote
git remote add upstream git@github.com:CoderDojoChi/c2.git

# Disable push for upstream
git remote set-url --push upstream DISABLE

# Build and run docker
docker-compose -f local.yml build
docker-compose -f local.yml up
```

---

## Running the App

```bash
# Running with log output
docker-compose -f local.yml up

# Running daemon mode (in the background)
docker-compose -f local.yml up -d

# Attaching a log output to already-running process
docker-compose -f local.yml logs django
docker-compose -f local.yml logs postgres
```

Load the website via [localhost:8000](http://localhost:8000) and going to [/admin/](http://localhost:8000/admin). The debug admin login info is:

Username: **admin@admin.com**\
Password: **coderdojochi**

---


## Management
For a full list of management options, start the app, then create a shell into the instance. the following commands:

```bash
# In one window
docker-compose -f local.yml up

# In another window
docker-compose -f local.yml run --rm django bash
invoke --list
```

---

## Adding Dependencies
Add the pip requirement to the appropriate file in `requirements/*.txt` (most likely `base.txt`).

---

## Migrations
```bash
# Create migrations
docker-compose -f local.yml run --rm django python manage.py makemigrations

# Save a single app's model as fixtures
docker-compose -f local.yml run --rm django python manage.py dumpdata APP.MODEL > coderdojochi/APP/fixtures/MODEL.json

# Run Migrations
docker-compose -f local.yml run --rm django python manage.py migrate

# Create a new app
docker-compose -f local.yml run --rm django python manage.py startapp APP_NAME

```
