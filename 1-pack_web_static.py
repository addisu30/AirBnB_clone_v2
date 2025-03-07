#!/usr/bin/python3
# fabfile to generate archive file
from fabric.api import local, env
from datetime import datetime

env.user = 'ubuntu'
env.hosts = ['54.237.44.125', '35.175.134.1']


def do_pack():
    """
    Targging project directory into a packages as .tgz
    """
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    local('sudo mkdir -p ./versions')
    path = './versions/web_static_{}'.format(now)
    local('sudo tar -czvf {}.tgz web_static'.format(path))
    name = '{}.tgz'.format(path)
    if name:
        return name
    else:
        return None
