from django.db import models
from django.db.models.base import Model

class Ticket(models.Model):
    raisedBy =models.ForeignKey(
        "Student", on_delete=models.CASCADE, null=True, blank=True
    )
    claimedBy=models.ForeignKey(
       "TA", on_delete=models.CASCADE, null=True, blank=True
    )
    room=models.IntegerField(default=None)
    lab_number = models.IntegerField(default=0)
    description = models.TextField(default="enter you question /problem here")
    createdDate=models.DateTimeField(auto_now=True)
    closedDate=models.DateTimeField(auto_now_add=True)
    state=models.CharField(max_length=256 ,default='pending ticket')
    rating=models.IntegerField(default=0)
    
    def __str__(self):
        return "{} - {}".format(self.raisedBy, self.ticket_id)

    class Meta:
        ordering = ["-createdDate"]


class TA(models.Model):
    name=models.TextField(default='None')
    
    def __str__(self):
       return self.name



class Student(models.Model):
    name=models.TextField(default='None')
    
    def __str__(self):
       return self.name

