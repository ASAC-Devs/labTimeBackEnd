from django.db import models
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.base import Model
from django.db.models.fields import DateTimeField
# from account.models import profile , courses 

# Create your models here.


class Session (models.Model):
    # account =models.ForeignKey(
    #     "account", on_delete=models.CASCADE, null=True, blank=True
    # )
    
    creationDate=models.DateTimeField(auto_now=True)
    expiryDate=models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return "{} - {}".format(self.creationDate)

  
