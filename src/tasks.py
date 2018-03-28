from invoke import task


@task
def start(ctx):
    build(ctx)
    migrate(ctx)
    load_dev_fixtures(ctx)

    # Must be last- this is a long running process
    serve(ctx)


@task
def build(ctx):
    ctx.run("./manage.py collectstatic --no-input")


@task
def migrate(ctx):
    ctx.run("./manage.py migrate")


@task
def serve(ctx):
    ctx.run("gunicorn dojo.wsgi -b 0.0.0.0:8000")


@task
def load_dev_fixtures(ctx):
    # TODO: Figure out which env var to inform when to load fixtures
    # Check to make sure this isn't being run in production
    ctx.run("./manage.py loaddata account/fixtures/*")


@task
def format(ctx):
    ctx.run("autopep8 -iaarj4 --exclude=\"*/migrations/*\" --max-line-length=\"120\" .")


@task
def test(ctx):
    format(ctx)
    # no_uncommitted_changed(ctx)
