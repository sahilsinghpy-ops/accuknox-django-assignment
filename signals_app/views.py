from django.http import HttpResponse
from .models import Demo,ThreadDemo,TransactionDemo,TransactionLog
import threading
from django.db import transaction

def create_demo(request):

    print("Before Save")

    Demo.objects.create(name="Sahil")

    print("After Save")

    return HttpResponse("Done")




def test_same_thread(request):

    print("View Thread ID:", threading.get_ident())

    ThreadDemo.objects.create(name="Question 2")

    return HttpResponse("Question 2 Done")


def test_transaction(request):

    try:

        with transaction.atomic():

            TransactionDemo.objects.create(
                name="Transaction Test"
            )

            raise Exception("Force Rollback")
    except Exception:

        print("Rollback Happened")

    print(
        "TransactionDemo Count:",
        TransactionDemo.objects.count()
    )

    print(
        "TransactionLog Count:",
        TransactionLog.objects.count()
    )

    return HttpResponse("Question 3 Done")
