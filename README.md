# smartcoops

We bring a marketplace and mobile banking to agricultural coops. Check out the wiki to learn more.

> http://github.com/dannycastonguay/smartcoops/wiki

## How to run the SMS Simulator

Assuming you are in a posix environment (linux, macos) and that you have cloned this project to your system.

> `% cd PATH-TO-PROJECT-DIR`

> `% cd pilot`

> `% python smsSimulator.py`

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

To run the smsSimulator: 

1. `python ~/antportal/smartcoops/pilot/smsSimulator.py`

To run the django app

1. `python ~/antportal/smartcoops/django manage.py syncdb`
1. `python ~/antportal/smartcoops/django manage.py runserver`





## Copyright

For the time being, all rights reserved to AntPortal Corp of Canada.

