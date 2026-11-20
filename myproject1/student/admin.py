from django.contrib import admin
from django.db.models import Avg, Max

from .models import Student_table

admin.site.site_header = "College Portal Admin"
admin.site.site_title = "College Portal"
admin.site.index_title = "Dashboard"


@admin.register(Student_table)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("reg_no", "name", "email", "marks", "date")
    list_display_links = ("reg_no", "name")
    search_fields = ("reg_no", "name", "email")
    list_filter = ("date",)
    ordering = ("reg_no",)
    list_per_page = 20
    date_hierarchy = "date"


# Send student numbers to the admin home page banner
_default_index = admin.site.index


def dashboard_index(request, extra_context=None):
    stats = Student_table.objects.aggregate(avg=Avg("marks"), top=Max("marks"))
    extra_context = extra_context or {}
    extra_context.update(
        student_count=Student_table.objects.count(),
        avg_marks=stats["avg"],
        top_marks=stats["top"],
    )
    return _default_index(request, extra_context)


admin.site.index = dashboard_index