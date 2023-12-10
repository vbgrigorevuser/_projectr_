from django.db import models

# Create your models here.
class Client(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ', tel: ' + self.phone

class Restaurant(models.Model):
    client = models.ForeignKey(Client, models.CASCADE)
    name = models.CharField(max_length=200)
    income = models.CharField(max_length=200)
    wastes = models.CharField(max_length=200)

    def __str__(self):
        return self.client.first_name +  self.client.last_name + \
               ', tel: ' + self.client.phone + ', income: ' + self.income + ', wastes: ' + self.wastes

class Research(models.Model):
    client = models.ForeignKey(Client, models.CASCADE)
    profit = models.CharField(max_length=200)

    def __str__(self):
        return self.client.first_name +  self.client.last_name + \
               ', tel: ' + self.client.phone + ', profit: ' + self.profit