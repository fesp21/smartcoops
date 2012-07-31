# smartcoops

We bring a marketplace and mobile banking to agricultural coops. Check out the [wiki to learn more](http://github.com/dannycastonguay/smartcoops/wiki)

## Manifest

There are currently two parts to this project. One is a Django web app that deploys to Heroku, and the other is a Python command line simulator for farmer interactions with the SMS server. At the moment, we need to manually add your phone number and you need to be using a Globe phone number to be able to interact with the application using SMS. Hopefully Smart will fix their issues and hopefully Globe will allow us to accept more phone numbers.

# SMS Simulator Installation

1. Install Python 2.7 or above (not Python 3.X unfortunately, since django does not support 3.X yet), if you are having trouble in MacOS try [these steps](http://myadventuresincoding.wordpress.com/2011/09/11/python-upgrading-python-with-easy_install-pip-and-virtualenv-on-a-mac/)
1. Install [git](http://git-scm.com/downloads)
1. Go to the folder where you want to code (in my examples, I type `cd ~/antportal/`)
1. `git clone git@github.com:dannycastonguay/smartcoops.git`

## Running the Simulator

1. `python ~/antportal/smartcoops/pilot/smsSimulator.py`

# Django app on Heroku Installation (works with Globe SMS)

1. `curl -O https://raw.github.com/pypa/virtualenv/master/virtualenv.py`
1. `python virtualenv.py scenv`  
1. `source ~/antportal/scenv/bin/activate`
1. `pip install django dj-database-url django-extensions psycopg2 pyglobe` (requirements come from the [dev center of Heroku](https://devcenter.heroku.com/articles/django))
1. If you are using MacOS, you might run into trouble with the installation of postgre, if so this [article might help you](http://stackoverflow.com/questions/846383/problem-installing-pyscopg2-on-mac-os-x)
1. Add your ssh key to heroku: `heroku keys:add` 
1. Add heroku to your list of remotes: `git remote add heroku git@heroku.com:tranquil-ocean-3872.git`
1. (Optional through recommended) set your local db to sqlite (especially if you couldn't get postgres installed propertly configured) `cp farmbook/rename2local_settings4sqlite.py farmbook/local_settings.py`

### Run the django app locally

1. Change directory to smartcoops (e.g. `cd ~/antportal/smartcoops/`)
1. Make sure you are in the virtual environment (`source ~/antportal/scenv/bin/activate`)
1. `python manage.py syncdb`
1. `python manage.py runserver`
1. Go to `127.0.0.1:8000` or `127.0.0.1:8000/admin` 
1. Change directory to sampleSMSCommand directory (e.g. `cd ~/antportal/smartcoops/sampleSMSCommand/`). To test sending SMS messages, modify `sms.xml` (or `cashVoucher.xml`) and use `curl -d @cashVoucher.xml http://localhost:8000/process/ | grep -A 20 Traceback:` (the `| grep -A 20 Traceback:` part is useful if you are debugging)

### Run the django app on heroku

1. Check that the django app runs locally
1. From the root of the directory, `git add` the files you have modified 
1. `git commit -m "some meaningful commit message"`
1. `git push` so your changes go to GitHub
1. `git push heroku master`
1. `heroku run python manage.py syncdb`
1. Check that it works by visiting the [home page](http://tranquil-ocean-3872.heroku.com) and the [admin page](http://tranquil-ocean-3872.heroku.com/admin) (username: danny, password: smartcoopsftw) on Heroku


## Copyright

For the time being, all rights reserved to [AntPortal Corp of Canada](http://www.antportal.com).

