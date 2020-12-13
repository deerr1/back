from django.contrib import admin

# Register your models here.
from Institutions import models 

admin.site.register(models.Subjects)
admin.site.register(models.Points)
admin.site.register(models.InfoInstitutions)