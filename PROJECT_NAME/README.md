![Docker-Django-React Template](https://s3.amazonaws.com/media-p.slid.es/uploads/176500/images/1488501/ddr.png)

## Requirements

1. Docker Engine and Compose
2. NPM

## Starting the Django Project
```bash
django-admin startproject \
  --template=https://github.com/SiliconValleyInsight/ddr-template/archive/master.zip \
  --extension=sh,py,yml,json \
  --name=package.json \
  PROJECT_NAME
# File permissions aren't being respected
# for some reason. I'll fix this later :P
chmod +x docker-entrypoint bin/*
```

## Development setup

### Configure

```
# dev.env
SECRET_KEY=
POSTGRES_PASSWORD=
```

### Install web dependencies

```bash
docker-compose run --rm web bin/install.sh
```

### Create services

```bash
docker-compose up -d
```

### Setup django

```bash
docker-compose run --rm web python manage.py migrate
docker-compose run --rm web python manage.py createsuperuser
```

## Production setup

WIP
