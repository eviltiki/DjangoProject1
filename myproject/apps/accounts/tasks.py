from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

@shared_task
def send_admin_notification(username):
    subject = 'Новый пользователь зарегистрирован'
    message = f'Пользователь с именем {username} зарегистрировался на сайте.'
    recipient_list = [settings.ADMIN_EMAIL]
    print('SEND MAIL')
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list)