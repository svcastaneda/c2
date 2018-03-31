from invoke import task
import os


@task
def release(ctx):
    collect_static(ctx)
    migrate(ctx)
    load_dev_fixtures(ctx)


@task(help={"port": "Port to use when serving traffic. Defaults to $PORT."})
def start(ctx, port=os.environ.get("PORT", 8000)):
    ctx.run(f"gunicorn dojo.wsgi -w 2 -b 0.0.0.0:{port} --reload")


@task
def migrate(ctx):
    ctx.run("python manage.py migrate")


@task
def load_dev_fixtures(ctx):
    # TODO: Figure out which env var to inform when to load fixtures
    # Check to make sure this isn't being run in production
    ctx.run("python manage.py loaddata account/fixtures/*")


@task
def collect_static(ctx):
    ctx.run("python manage.py collectstatic --no-input")


@task
def format(ctx):
    ctx.run("autopep8 -iaarj4 --exclude=\"*/migrations/*\" --max-line-length=\"120\" .")


@task
def test(ctx):
    format(ctx)
