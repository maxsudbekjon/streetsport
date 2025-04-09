mig:
	python3 manage.py makemigrations
	python3 manage.py migrate
create_user:
	python3 manage.py createsuperuser