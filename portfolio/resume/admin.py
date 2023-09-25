from django.contrib import admin
from .models import Chef,Testimonials



class ChefsAdmin(admin.ModelAdmin):
    list_display=["name","job_possition","text","images"]
    list_filter=["name","text"]
    
    
class TestimonialsAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'position')
    search_fields = ('full_name', 'position')
    
# Register your models here.
admin.site.register(Chef,ChefsAdmin)
admin.site.register(Testimonials,TestimonialsAdmin)

