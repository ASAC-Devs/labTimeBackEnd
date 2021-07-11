from django.contrib import admin
from .models import Student, Ticket,TA

admin.site.register(Ticket)
admin.site.register(Student)
admin.site.register(TA)