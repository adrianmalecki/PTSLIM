from django.contrib import admin
from .models import Patient, Personaldata, Doctor, Reservation

admin.site.register(Personaldata)
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Reservation)

