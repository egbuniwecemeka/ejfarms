"""
    Fabfile to:
        - update the remote system
        - Install and download dependencies and applications
"""

"""
    Fabric installation
        - sudo apt update
        - sudo apt install python3-pip
        - pip3 install fabric
        - fabric --version
"""

# Import Fabric's API module
from fabric.api import env, run

env.hosts = ['server.domain.tld', 'server1.domain.tld']

# set the username
env.user = "ej"

# Set the password [NOT RECOMMENDED] - prompt for password to avoid hardcoding
# env.password = prompt("Enter your password: ")
# Set password using SSH (Optional only if not default SSH file)
env.key_filename = "~/ssh/school"

def update_upgrade():
    """Update the default OS configuration"""
    run("apt update")
    run("apt -y upgrade")

def install_memcached():
    """Download and install memcached"""
    run("aptitude install -y memcached")

def update_install():
    """Update OS config & install memcached"""
    update_upgrade()
    install_memcached()
