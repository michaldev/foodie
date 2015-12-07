#!/usr/bin/env bash

apt-get update -y

echo "Installing system packages"
apt-get install -y build-essential python-pip python-dev mc git

# Dependencies for virtualenv
apt-get install -y libjpeg8 libjpeg8-dev libtiff-dev zlib1g-dev libfreetype6-dev liblcms2-dev libxml2-dev libxslt1-dev libssl-dev swig libyaml-dev libpython2.7-dev


# setup postgresql in virtual machine
echo "Setup postgresql in virtual machine"

if ! command -v psql; then
    apt-get install -y postgresql
    apt-get -y install postgresql-server-dev-all
    cp /vagrant/provisioning/templates/pg_hba.conf /etc/postgresql/9.3/main/
    service postgresql reload

    su - postgres -c "createuser -d -s vagrant"
    sudo -u postgres psql -U postgres -d postgres -c "ALTER USER vagrant WITH PASSWORD 'vagrant';"
    #createdb -O rolename dbname
    sudo -u postgres -c "createdb -O vagrant vagrant"
    #echo "Importing db"
    #su - vagrant -c "psql -U vagrant -d vagrant -f /vagrant/provisioning/vagrant.sql"
fi

# Dependencies for JS stuff
apt-get install -y nodejs npm

## fix paths
ln -s /usr/bin/nodejs /usr/bin/node

# SASS COMPASS support
gem install compass

# Swap to overcome errors during the installation of lxml
swapfile="/swapfile"
if [ ! -f "$swapfile" ]
then
    fallocate -l 4G /swapfile
    chmod 600 $swapfile
    mkswap $swapfile
    swapon $swapfile
    echo "/swapfile     none    swap    sw      0       0" |tee -a /etc/fstab
fi

echo "Setup pip and virtualenv"
pip install virtualenv
pip install virtualenvwrapper
pip install envdir
