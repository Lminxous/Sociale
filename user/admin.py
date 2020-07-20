from django.contrib import admin
from .models import Profile,Circle
# from import_export.admin import ImportExportModelAdmin



admin.site.register(Profile)
admin.site.register(Circle)

# @admin.register(Profile,Circle)
# class ViewAdmin(ImportExportModelAdmin):
#     pass
