from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Destination)
admin.site.register(Contact)
admin.site.register(ConfirmBooking)

admin.site.register(Payment)


admin.site.register(Cancellation)