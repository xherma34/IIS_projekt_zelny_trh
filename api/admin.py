from django.contrib import admin


# Register your models here.
from .models import *

admin.site.register(User)
admin.site.register(Crop)
admin.site.register(CropCatalog)
admin.site.register(Harvest)
admin.site.register(HarvestUsers)
admin.site.register(Order)
admin.site.register(OrderDetail)
admin.site.register(Suggestion)
