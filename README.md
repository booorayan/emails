# Send Async Mails with Celery, Celery Beat and Redis

In this django project, we employ celery, redis and celery beat to asynchronously send mail notifications to users.
A user enters an email to receive notifications and also provides the message/notification to be sent to the provided email.

Celery is often used in Django applications to manage and run background tasks such as image processing and email notifications. 
It works by sending messages between django apps and worker processes through a message broker, like Redis or RabbitMQ.
Celery beat is responsible for handling periodic/scheduled tasks.

Redis is a temporary in-memory data store that can serve as a message broker for task queue systems like celery.
It stores the tasks in a queue and celery workers consume the tasks.

The project executes two simple tasks defined in tasks.py:

1. Sends an email notification to a user's email after they subscribe to receive email notifications.
2. Sends an email daily at 14:30pm to the listed recipient email accounts.

To run the project, clone the project, activate the virtual environment and do the following:

Install project requirements/dependencies:

`pip install -r requirements.txt`

Run migrations: 

`python manage.py migrate`

Run the server: 

`python manage.py runserver`

Run celery:

`celery -A mails worker -l info`

Run celery beat:

`celery -A mails beat -l INFO`

Access the website at: https://127.0.0.1:8000/
