from django.core.mail import send_mail
from django.utils.html import format_html
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def send_confirmation_email(email, code):
    activation_url = f'http://13.60.35.3:8000/api/user/activate/?u={code}'
    context = {
        'activation_url': activation_url
    }
    
    msg_html = render_to_string('index.html', context)
    message = strip_tags(msg_html)
    send_mail(
        'Account activation',
        message,
        'test@gmail.com',
        [email],
        html_message=msg_html,
        fail_silently=False
    )


def send_password_reset_email(email, code):
    password_reset_url = f'{code}'
    message = format_html(
        'Здравствуйте, Ваш код подтверждения:'
        ' {} ',
        password_reset_url
    )


    send_mail(
        'Здравствуйте',
        message,
        'test@gmail.com',
        [email],
        fail_silently=False
    )