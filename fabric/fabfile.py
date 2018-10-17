
"""
Deploy script for Academis on PythonAnywhere
"""

from fabric.api import local, lcd, cd, env
from fabric.api import run
import os

env.hosts = ['ssh.pythonanywhere.com']

def deploy():
    """Load all articles to database on server"""
    with cd('academis'):
        run("git pull")
    with cd('academis_bottle'):
        run("python3 add_posts.py")

def rebuild():
    """
    Updates server code, 
    deletes database and 
    creates it from scratch"""
    with cd('academis_bottle'):
        run("git pull")
        run("rm academis.db")
        run("python3 dbhelper.py")
    deploy()
    print("PLEASE RESTART WEB SERVICE MANUALLY!")
