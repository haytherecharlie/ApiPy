from invoke import task

@task
def serve(c):
    c.run("python3 -B server/server.py") # No __pycache__.py files