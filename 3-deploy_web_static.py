#!/usr/bin/python3
""" Fabric script that creates and distributes an archive to web servers """
from fabric.api import *
from datetime import datetime
from os import path

env.hosts = ['100.26.178.116', '54.144.154.1']


def do_pack():
    """ script that generates a .tgz archive """
    date_time = datetime.now().strftime("%Y%m%d%H%M%S")

    local("mkdir -p versions")
    archive = "versions/web_static_{}.tgz".format(date_time)

    if local("tar -czvf {} web_static".format(archive)).succeeded:
        return archive
    else:
        return None


def do_deploy(archive_path):
    """
    function distributes an archive to web servers
    """
    if not path.exists(archive_path):
        return False

    try:
        file_name = archive_path.split('/')[-1]
        file_base = file_name.split('.')[0]
        path_static = "/data/web_static/releases/{}/".format(file_base)

        put(archive_path, '/tmp/')

        run("mkdir -p {}".format(path_static))

        run("tar -xzf /tmp/{} -C {}".format(file_name, path_static))

        run("rm /tmp/{}".format(file_name))
        run("mv {}web_static/* {}".format(path_static, path_static))
        run("rm -rf {}web_static".format(path_static))
        run("rm -rf /data/web_static/current")

        run("ln -s {} /data/web_static/current".format(path_static))
        print("New vision deployed")

        return True
    except Exception:
        return False


def deploy():
    """ Function that distributes an archive to web servers. """
    archive_path = do_pack()

    if not archive_path:
        return False
    else:
        return do_deploy(archive_path)
