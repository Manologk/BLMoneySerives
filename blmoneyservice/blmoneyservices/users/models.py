from django.db import models


# Create your models here.
class Client(models.Model):
    # client_id = models.CharField(primary_key=True, autoincrement=True)
    name = models.CharField(max_length=25)
    email = models.EmailField(max_length=30, default=None, null=False, blank=False)
    phone = models.CharField(max_length=25, default=None, null=False, blank=False)
    password = models.CharField(max_length=15)


class RecipientRusZam(models.Model):
    fullname = models.CharField(max_length=30, null=False, blank=False)
    phoneNumber = models.CharField(max_length=25, null=False, blank=False)


class Transaction(models.Model):
    # trans_id = models.CharField(primary_key=True, autoincrement=True)
    trans_type = models.CharField(max_length=30)
    amount = models.IntegerField()
    cli_id = models.ForeignKey(Client, blank=True, null=True, on_delete=models.CASCADE)


class TransactionDetails(models.Model):
    recipient_phone = models.CharField(max_length=25)
    statuses = (
        ('P', 'Processing'),
        ('T', 'Transit'),
        ('C', 'Completed')
    )
    status = models.CharField(max_length=15, choices=statuses, null=True)
    transaction_id = models.ForeignKey(Client, blank=True, null=True, on_delete=models.CASCADE)
    field = models.CharField(max_length=100)
