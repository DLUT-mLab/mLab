sync:
	virtualenv venv;
	. venv/bin/activate;\
	pip install -r pip-req.txt;\
	./manage.py migrate

serve:
	. venv/bin/activate;\
	./manage.py runserver

deploy:
	. venv/bin/activate;\
	./manage.py runserver 0.0.0.0:80
