pip install -r examples/requirements.txt
python setup.py install
mkdir -p examples/logs examples/db examples/media examples/media/static
python examples/example/manage.py collectstatic --noinput
python examples/example/manage.py syncdb --noinput
python examples/example/manage.py migrate --noinput
