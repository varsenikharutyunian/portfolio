from django.db import models

# Create your models here.
class Chefs(models.Model):
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
    