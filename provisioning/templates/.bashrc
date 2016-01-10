export WORKON_HOME=~/envs
source /usr/local/bin/virtualenvwrapper.sh

export PATH=$HOME/.node/bin:$PATH

workon vagrant
cd /vagrant
alias rs='/vagrant/manage.py runserver 0.0.0.0:8000'
