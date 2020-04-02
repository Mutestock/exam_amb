import click
from rest.endpoints import flask_run
import sys
from logic.basic import retrieve_environment

# pip install --editable .
# Preferably inside virtual environment to prevent clogging up the global modules.

@click.group()
def amb():
    '''
    Ambience project CLI 
    '''

@amb.command()
@click.option("-os", is_flag=True, help= "Returns OS of the PC")
@click.option("--environment", '-e', is_flag=True, help="Returns current environment type. Synced on call")
def stats(os, environment):
    '''
    Shows current setup options
    '''
    if(os):
        click.echo(f"OS: {sys.platform}")
    if(environment):
       click.echo(f"Environment: {retrieve_environment()}")

@amb.command()
def launch():
    '''
    Runs backend server
    ''' 
    flask_run()