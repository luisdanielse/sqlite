from __future__ import absolute_import, unicode_literals
from .celery import app
from django.core.mail import send_mail
from orders.models import Order


@app.task
def order_created(order_id):

    """
    Task to send an e-mail notification when an order is successfully created.
    """
    order = Order.objects.get(id=order_id)
    subject = 'Orden no. {}'.format(order.id)
    message = 'Querido {},\n\n Tu orden ha sido recibida exitosamente. Rastrea tu orden con el id:  {}.'.format(order.first_name,
                                                                             order.id)
    mail_sent = send_mail(subject, message, 'admin@myshop.com', [order.email])
    return mail_sent
