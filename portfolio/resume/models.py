from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Skill(models.Model):
    name = models.TextField(max_length=30)
    value = models.PositiveIntegerField(validators=[MaxValueValidator(100), MinValueValidator(1)], default=1)
    
    def __str__(self) -> str:
        
        return f"{self.name} skill value is {self.value}"
    
    
class Education(models.Model):
    university_name = models.TextField(max_length=70)
    start_date = models.PositiveIntegerField(validators=[MaxValueValidator(2023), MinValueValidator(1900)])
    end_date = models.PositiveIntegerField(validators=[MaxValueValidator(2023), MinValueValidator(1900)])
    grade = models.TextField(max_length=30, blank=True, null=True)
    created_on=models.DateTimeField(auto_now=True)
    
    
    def __str__(self) -> str:
        return f"{self.university_name} university grade is {self.grade}"
    
    
    
class Experience(models.Model):
    job_possition=models.TextField()
    start_data=models.PositiveIntegerField(validators=[MaxValueValidator(2023), MinValueValidator(1900)])
    end_data=models.PositiveIntegerField(validators=[MaxValueValidator(2023), MinValueValidator(1900)])
    is_current=models.BooleanField()
    addres=models.TextField(max_length=70)
    job_description=models.TextField()
    company_name=models.TextField(max_length=70)
    compani_logo=models.ImageField()
        
    def __str__(self) -> str:
        return f"{self.company_name} company, job_possition {self.job_possition}"

class SocialMedia(models.Model):
    platform_name = models.TextField()
    url = models.TextField()

    def __str__(self) -> str:
        return f"{self.platform_name} account"
    

class Testimonial(models.Model):
    name = models.TextField()
    proffesion = models.TextField()
    text = models.TextField()
    image =models.ImageField()
    
    def __str__(self) -> str:
        return f"{self.name} - {self.proffesion}"

class Service(models.Model):
    service_name = models.TextField()
    service_description = models.TextField()  
    
    def __str__(self) -> str:
        return f"{self.service_name} - {self.service_description}"
        
    
class languages(models.Model):
    title = models.TextField()
    def __str__(self) -> str:
        return f"{self.title}"
            

    