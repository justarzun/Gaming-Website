from django.db import models


# Create your models here.
class ContactForm(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=250)


    def __str__(self):
        return self.name + self.email + self.subject + self.message
