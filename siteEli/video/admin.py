from django.contrib import admin
from .models import Video, Cover, Performer

# Register your models here.
admin.site.register(Video)
admin.site.register(Cover)
admin.site.register(Performer)