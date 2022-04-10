from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/index.py")

@task 
def test(ctx):
    ctx.run("pytest src -vv")

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src -v")

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html")

@task
def lint(ctx):
    ctx.run("pylint src")