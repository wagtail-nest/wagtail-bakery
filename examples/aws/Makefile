all: clean install migrate loaddata runserver

clean:
	find . -name '*.pyc' | xargs rm
	rm -rf build/ example/public/ example/db.sqlite3

install:
	pip install -r requirements.txt

migrate:
	python manage.py migrate

loaddata:
	python manage.py loaddata fixtures/users.json
	python manage.py loaddata fixtures/pages.json
	python manage.py loaddata fixtures/sites.json

dumpdata:
	python manage.py dumpdata auth.User --indent=2 --natural-foreign > fixtures/users.json
	python manage.py dumpdata example wagtailcore.Page --indent=2 --natural-foreign > fixtures/pages.json
	python manage.py dumpdata wagtailcore.Site --indent=2 --natural-foreign > fixtures/sites.json

runserver:
	python manage.py runserver
