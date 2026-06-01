from django.db import models


class Demo(models.Model):
    name = models.CharField(max_length=100)


class ThreadDemo(models.Model):
    name = models.CharField(max_length=100)


class TransactionDemo(models.Model):
    name = models.CharField(max_length=100)


class TransactionLog(models.Model):
    message = models.CharField(max_length=100)