from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Chef(models.Model):
    name=models.TextField(max_length=50)
    job_possition = models.TextField()
    text= models.TextField()
    images=models.ImageField(upload_to="img")
    
    def __str__(self) -> str:
        return f"{self.name} is {self.images}"
    
    
class Testimonials(models.Model):
    full_name = models.TextField(max_length=30)
    position = models.TextField(max_length=70)
    testimonial = models.TextField(max_length=300)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    # link = models.URLField(blank=True, null=True)
    

    def __str__(self) -> str:
        return f"Name - {self.full_name}"
    
class PersonalInfo(models.Model):
    website = models.URLField(max_length = 200)
    phone = models.CharField(max_length=30)  
    degree = models.CharField(max_length=30)
    email = models.EmailField()
    adres = models.CharField(max_length=30)
    openinghours=models.TextField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Message(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=1000)
    