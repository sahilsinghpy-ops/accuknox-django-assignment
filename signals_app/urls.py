from django.urls import path
from .views import create_demo,test_same_thread,test_transaction

urlpatterns = [
    path("test/", create_demo),          # Question 1
     path("test2/", test_same_thread),
     path("test3/", test_transaction),
]