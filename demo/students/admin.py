from django.contrib import admin

from students.models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ('lastname', 'graduation')
    list_filter = ('graduation', )
    search_fields = ('firstname', 'lastname')


admin.site.register(Student, StudentAdmin)
