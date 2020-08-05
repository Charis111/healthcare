from django.db import models
from datetime import datetime

# Create your models here.

class MainCategory(models.Model):
    """docstring for MianCategory"""

    main_category=models.CharField(max_length=200)
    cat_summary = models.CharField(max_length=1000)
    cat_slug = models.CharField(max_length=200)
    image=models.ImageField( default = 'img/img.jpg')

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.main_category

    def snippet(self):
        return self.cat_summary[:100] + '...'




class Specialization(models.Model):
    speciality = models.CharField(max_length=200)
    main_category = models.ForeignKey(MainCategory, default=1, verbose_name="Category", on_delete=models.SET_DEFAULT)
    series_summary = models.CharField(max_length=200)
    image=models.ImageField( default = 'img/img.jpg')

    class Meta:
        verbose_name_plural = "MainFeild"

    def __str__(self):
        return self.speciality

    def snippet(self):
        return self.series_summary[:50] + '...'





class DoctorFullProfile(models.Model):
    Male = 'M'
    Female = 'F'
    

    SEX= [
        (Male, 'M'),
        (Female, 'F'),    
    ]

    Full_name=models.CharField(max_length=200)
    Specialize=models.CharField(max_length=200)
    Sex=models.CharField(max_length=200,choices=SEX,)
    DateOfBirth=models.DateField()
    Phone_Number=models.IntegerField()
    Address=models.CharField(max_length=200)
    Google_Address=models.CharField(max_length=200)

    
    main_content = models.TextField()
    date_published = models.DateTimeField("date published", default=datetime.now())

    speciality = models.ForeignKey(Specialization, default=1, verbose_name="MainFeild", on_delete=models.SET_DEFAULT)
    doctor_slug = models.CharField(max_length=200, default=1)
    CoverPhoto = models.ImageField(default='default.jpeg', blank=True)
    ProfilePic = models.ImageField(default='doc...jpg', blank=True)

    def __str__(self):
        return self.main_content


    def snippet(self):
        return self.main_content[:50] + '...'
