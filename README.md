# smartcoops

We bring a marketplace and mobile banking to agricultural coops. Check out the wiki to learn more.

> http://github.com/dannycastonguay/smartcoops/wiki

## Manifest

There are currently two parts to this project. One is a Django web app that deploys to Heroku, and the other is a Python command line simulator for farmer interactions with the yet to be built SMS server.

## Installation

1. Install Python 2.5 or above (not Python 3.X unfortunately, since django does not support 3.X yet)
1. Install [git](http://git-scm.com/downloads)
1. Go to the folder where you want to code (in my examples, I type `cd ~/antportal/`)
1. `git clone git@github.com:dannycastonguay/smartcoops.git`
2. `curl -O https://raw.github.com/pypa/virtualenv/master/virtualenv.py`
1. `python virtualenv.py scenv`  
1. `source ~/antportal/scenv/bin/activate`
1. `pip install django`
1. `pip install dj-database-url`
1. `pip install django-extensions`

### Run the smsSimulator

1. `python ~/antportal/smartcoops/pilot/smsSimulator.py`

### Run the django app

1. `python ~/antportal/smartcoops/django manage.py syncdb`
1. `python ~/antportal/smartcoops/django manage.py runserver`

### Run the django app on heroku

1. Install postgre (to be able to run locally) http://stackoverflow.com/questions/846383/problem-installing-pyscopg2-on-mac-os-x
1. Follow instructions at https://devcenter.heroku.com/articles/django

## Copyright

For the time being, all rights reserved to AntPortal Corp of Canada.

