.PHONY: clean system-packages python-packages install tests run all

clean:
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.log' -delete

system-packages:
	sudo apt install python-pip -y

python-packages:
	pip install -r requirements.txt --no-cache-dir

install: system-packages python-packages

tests:
	python manage.py test

init-db:
	python manage.py db init
	python manage.py db migrate --message 'initial database migration'
	python manage.py db upgrade

run:
	python manage.py run

all: clean install tests init-db run
