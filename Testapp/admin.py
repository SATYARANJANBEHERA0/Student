from django.contrib import admin

from Testapp.models import Student
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['Firstname','Lasttname','Email','Password','Occupation','Gender','DOB','Education','State','Country']
admin.site.register(Student,StudentAdmin)
