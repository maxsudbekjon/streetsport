from django.contrib import admin
from django.contrib import admin
from django.utils.html import format_html
from .models import Stadium
from apps.models import User, Stadium

# Register your models here.
admin.site.register(User)


class StadiumAdmin(admin.ModelAdmin):
    list_display = ('__str__',)

    def changelist_view(self, request, extra_context=None):
        stadium_count = Stadium.objects.count()
        extra_context = extra_context or {}
        extra_context['title'] = f"Ro'yxatdan o'tgan Stadionlar soni :  {stadium_count} ta"
        return super().changelist_view(request, extra_context=extra_context)

admin.site.register(Stadium, StadiumAdmin)
