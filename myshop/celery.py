import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myshop.settings')


app = Celery('myshop',
             broker='amqp://guest@localhost//',
             include=['myshop.tasks'])



app.conf.update(
    result_expires=3600,
)

if __name__ == '__main__':
    app.start()
