from celery import shared_task
from django.core.mail import send_mail
from mails import settings


# send notification mail
@shared_task(bind=True)
def send_notification_mail(self, target_mail, message):
    mail_subject = 'Welcome on board!!'
    send_mail(
        subject=mail_subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[target_mail],
        fail_silently=False,
    )

    return 'Done'


# task to send mail periodically, i.e., daily at 12:36pm
@shared_task(bind=True)
def send_periodic_mails(self, message):
    recipient_list = ['bryantlch@gmail.com', 'brian.ouma@8teq.co.ke']
    mail_subject = 'Have A Great Day!!'
    send_mail(
        subject=mail_subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=recipient_list,
        fail_silently=False,
    )

    return 'Done Done'
