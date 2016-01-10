#!/usr/bin/env bash


# JS setup
echo "Setup JS"
echo prefix = ~/.node >> ~/.npmrc
# install grunt packages
npm install grunt grunt-cli bower -g

echo "Create virtualenv"
mkdir /home/vagrant/envs
export WORKON_HOME=~/envs
source /usr/local/bin/virtualenvwrapper.sh
mkvirtualenv vagrant

pip install -r /vagrant/requirements.txt

cd /vagrant
chmod +x manage.py
./manage.py migrate --noinput

cd /vagrant
bower install --config.interactive=false

cp -p /vagrant/provisioning/templates/.bashrc /home/vagrant/.bashrc

echo "Finished!"
echo "Please run 'vagrant ssh' to ssh to dev machine"
echo "Then run 'rs' to start django (in virtual machine, after vagrant ssh was called)"
echo "Then go to localhost:8000 in the browser (on the host, not in virtual machine)"
