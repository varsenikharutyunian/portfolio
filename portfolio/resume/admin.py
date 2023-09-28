from django.contrib import admin
from .models import Chef,Testimonials,Message,PersonalInfo



class ChefsAdmin(admin.ModelAdmin):
    list_display=["name","job_possition","text","images"]
    list_filter=["name","text"]
    
class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'firstname','lastname','surname','jobe' 'address', 'tel', 'email']
    list_filter = ['name']
    search_fields = ['name']
    
    
class TestimonialsAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'position')
    search_fields = ('full_name', 'position')
    
# Register your models here.
admin.site.register(Chef,ChefsAdmin)
admin.site.register(Testimonials,TestimonialsAdmin)
admin.site.register(PersonalInfo)
admin.site.register(Message)

