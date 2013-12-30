Gradebook
=========

A Django-based gradebook backed by the database of your choice
(SQLite3 begin the default)

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

You must have Django installed. You will also want to have
django-zurb-foundation installed (I am using version 5.0.2).

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

Running
=======

From the gradebook/ directory, run the command `python manage.py
runserver` to run locally. Then in the browser, go to
http://localhost:8000/grades/.

Notes
=====

The example database is configured with user `admin` with password
`admin`. If you are using this for anything more than a toy, I suggest
changing both the username and password via the admin panel (go to
http://localhost:8000/admin/, log in, go to the Users section, and
edit the `admin` user to change the name. Use the "Change Password"
link at the top-right to change the password.