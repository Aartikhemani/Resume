from django.db import models
from django.core.validators import RegexValidator
# Create your models here.


class Home(models.Model):
    name = models.CharField(max_length=100)
    greeting1 = models.CharField(max_length=10)
    greeting2 = models.CharField(max_length=10)
    picture = models.ImageField(upload_to='picture/',blank=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'home'
        verbose_name_plural = 'homes'

    def __str__(self):
        return self.name


class About(models.Model):
    email = models.EmailField(max_length=200, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True, validators=[
        RegexValidator('^\\+?[0-9]{9,15}$', 'Enter a valid phone number.')])
    heading = models.CharField(max_length=50)
    career = models.CharField(max_length=50)
    description = models.TextField(blank=False)
    profile_img = models.ImageField(upload_to='profile/')
    update = models.DateTimeField(auto_now=True)
    cv = models.FileField(blank=True, null=True, upload_to="cv")
    certificate = models.FileField(blank=True, null=True, upload_to="certificate")

    def __str__(self):
        return self.career


class Profile(models.Model):
    about = models.ForeignKey(About,on_delete=models.CASCADE)
    social_name = models.CharField(max_length=20)
    social_logo = models.ImageField(upload_to='logo/', blank=True, null=True)
    link = models.URLField(max_length=200)

class Social(models.Model):
    about = models.ForeignKey(About,on_delete=models.CASCADE,null=True)
    social_name = models.CharField(max_length=50)
    social_logo = models.ImageField(upload_to='logo/', blank=True, null=True)
    link = models.URLField(max_length=200)


class Category(models.Model):
    name = models.CharField(max_length=100)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'skill'
        verbose_name_plural = 'skills'

    def __str__(self):
        return self.name


class Skills(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=50)


class Portfolio(models.Model):
    image = models.ImageField(upload_to='portfolio/')
    link = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f'Portfolio {self.id}'


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    message = models.TextField()