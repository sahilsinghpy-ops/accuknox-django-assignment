from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Demo,ThreadDemo,TransactionLog,TransactionDemo
import time,threading
print("signals.py loaded")

@receiver(post_save, sender=Demo)
def test_signal(sender, instance, **kwargs):

    print("Signal Started")

    time.sleep(5)

    print("Signal Finished")


@receiver(post_save, sender=ThreadDemo)
def thread_signal(sender, instance, **kwargs):

    import threading

    print("Signal Thread ID:", threading.get_ident())


@receiver(post_save, sender=TransactionDemo)
def transaction_signal(sender, instance, **kwargs):

    print("Transaction Signal Fired")

    TransactionLog.objects.create(
        message="Created from signal"
    )

    print("TransactionLog Created")
