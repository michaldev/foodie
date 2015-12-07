export WORKON_HOME=~/envs
source /usr/local/bin/virtualenvwrapper.sh

export PATH=$HOME/.node/bin:$PATH

workon vagrant
cd /vagrant/foodie
alias rs='/vagrant/foodie/manage.py runserver 0.0.0.0:8000'
