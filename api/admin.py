from django.contrib import admin
from .models import Pupil,Contact,Course,Group
# Register your models here.

admin.site.register(Pupil)
admin.site.register(Course)
admin.site.register(Contact)
admin.site.register(Group)
