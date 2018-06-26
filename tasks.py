from invoke import task

@task
def virtualize(c):
	c.run("source venv/bin/activate") # Enter virtual env

@task
def requirements(c):
	c.run("pip3 install -r requirements.txt") # Install Requirements

@task
def serve(c):
    c.run("python3 -B server/server.py") # No __pycache__.py files