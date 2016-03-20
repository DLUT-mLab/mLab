sync:
	virtualenv venv;
	. venv/bin/activate;\
	pip install -r pip-req.txt;\

serve:
	. venv/bin/activate;\
	./manage.py runserver

deploy:
	. venv/bin/activate;\
	./manage.py runserver 0.0.0.0:80

beansdb:
	beansdb -p 7900 -H /opt/beansdb -T 0 -v -L /home/linwei/workspace/python_workspace/beansdb/beansdb_log.conf

clean:
	find -type f -name '*.pyc' -delete
	rm -rf venv/  