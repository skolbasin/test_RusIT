run:
	python manage.py runserver

pep8:
	flake8 --statistics --count

superuser:
	./manage.py create_repair_superuser superuser super@luser.io

migrate:
	python manage.py makemigrations $(APP) && python manage.py migrate