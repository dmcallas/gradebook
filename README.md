Gradebook
=========

A Django-based gradebook backed by the database of your choice
(SQLite3 being the default)

Caveats
=======

This is currently a very early version. I would not recommend using it
for production purposes. If you do, I suggest backing up your database
after every major operation. My preference is to use SQLite and send
e-mail an encrypted copy of the database file to myself after every
major assignment has been entered.

Installation
============

Dependencies
------------

* You need to have Python 3. In the commands below, be sure to use the `pip` for Python 3 if you have multiple Python versions installed.
* You must have Django installed. 
* `pip install django-zurb-foundation`
* `pip install djangorestframework`
* `pip install markdown`
* `pip install django-filter`
* You need to either have South installed (`pip install South`) or remove it from the INSTALLED_APPS list.

Configuration
-------------

Update the `settings.py` file as appropriate. If you are using a
database other than SQLite3 you will need to add your database
settings.

If you wish to use, for example, PostgreSQL, look at old versions of
`settings.py` to see how I had it configured for local testing.

If you are not starting with the example database you will need to
initialize the database you are using. Navigate to the directory with
the `manage.py` file and run the command `python manage.py syncdb` after 

If you are using the example database, you will want to change
`settings.py` database setting from `'NAME': '../../../grades/gradebook.db'` to
`'NAME': 'gradebook.db.example'`

Running
=======

From the gradebook/ directory, run the command `python manage.py
runserver` to run locally. Then in the browser, go to
<http://localhost:8000/grades/>.

Notes
=====

The example database is configured with user `admin` with password
`admin`. If you are using this for anything more than a toy, I suggest
changing both the username and password via the admin panel (go to
<http://localhost:8000/admin/>, log in, go to the Users section, and
edit the `admin` user to change the name. Use the "Change Password"
link at the top-right to change the password.

License
=======

This project is licensed under AGPLv3
(http://www.gnu.org/licenses/agpl-3.0.html).

If you believe you have a compelling reason I should relicense
_portions_ of the application under a different flavor of GNU license
(GPL or LGPL), please feel free to contact me with your rationale.
