default: run

setup:
	pip install --upgrade flask flask-sqlalchemy flask-wtf flask-login flask-markdown python-dateutil python-ldap raven blinker flask-gravatar flask-babel flask-migrate scrypt

init:
	python2 scripts/init.py

seed:
	python2 scripts/seed.py

run:
	python2 manage.py runserver

i18n-update:
	pybabel extract -F babel.cfg -k lazy_gettext -o messages.pot .
	pybabel update -i messages.pot -d dudel/translations

i18n-compile:
	pybabel compile -d dudel/translations
