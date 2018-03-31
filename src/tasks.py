from invoke import task


@task
def release(ctx):
    migrate(ctx)
    load_dev_fixtures(ctx)


@task
def start(ctx):
    build(ctx)
    serve(ctx)


@task
def build(ctx):
    ctx.run("python manage.py collectstatic --no-input")


@task
def serve(ctx):
    ctx.run("gunicorn dojo.wsgi -w 2 -b 0.0.0.0:8000 --reload")


@task
def migrate(ctx):
    ctx.run("python manage.py migrate")


@task
def load_dev_fixtures(ctx):
    # TODO: Figure out which env var to inform when to load fixtures
    # Check to make sure this isn't being run in production
    ctx.run("python manage.py loaddata account/fixtures/*")


@task
def format(ctx):
    ctx.run("autopep8 -iaarj4 --exclude=\"*/migrations/*\" --max-line-length=\"120\" .")


@task
def test(ctx):
    format(ctx)
