#!/bin/bash

set -ex

if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

source ./envs 

debootstrap --include $PACKAGES $SUITE $TARGET

test -e $TARGET/usr/src/pystemd || git clone https://github.com/facebookincubator/pystemd $TARGET/usr/src/pystemd 

$NSPAWN bash -c 'yes socal | passwd'

$NSPAWN bash -c 'cd /usr/src/pystemd && rm -rf dist/* && python3 setup.py bdist_wheel && pip3 install dist/* || /bin/true'

exit 0
# pacman -Su --noconfirm
pacman  --noconfirm -S cython ipython python-pip python-wheel vim git debootstrap pandoc

pip install pypandoc Pygments

# lets install debian in the background
systemd-run --unit install-debian.service /usr/bin/debootstrap --include "dbus,vim" unstable /var/lib/machines/debian

# install pystemd

cd /usr/src/pystemd && rm -rf dist/* && python setup.py bdist_wheel && pip install dist/* || /bin/true

mkdir -p /usr/share/venvs.conf

cat <<EOT > /usr/share/venvs.conf/pyvenv-wo-site-packages.cfg
home = /usr/bin
include-system-site-packages = false
version = 3.6.5
EOT

cat <<EOT > /usr/share/venvs.conf/pyvenv-w-site-packages.cfg
home = /usr/bin
include-system-site-packages = true
version = 3.6.5
EOT

cat <<EOT >> /home/vagrant/.bashrc

test -e /var/lib/machines/debian/etc/os-release ||  systemctl -q is-active install-debian.service ||\
    sudo systemd-run --unit install-debian.service /usr/bin/debootstrap --include "dbus,vim" unstable /var/lib/machines/debian || /bin/true

test -z "\${INVOCATION_ID}" && sudo tmux

EOT


cat <<EOT >> /root/.bashrc

cd /srv/pycon

EOT
