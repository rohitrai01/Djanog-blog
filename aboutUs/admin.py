from django.contrib import admin
from .models import About,SocialLink
# Register your models here.

class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        obj_count = About.objects.all().count()
        if obj_count == 0:
            True
        else:
            False
        
admin.site.register(About,AboutAdmin)
admin.site.register(SocialLink)