from django.db import models

class ClothingPreference(models.Model):
    AGE_CHOICES = [
        ('30-40', '30-40'),
        ('40-50', '40-50'),
        ('50-60', '50-60'),
    ]
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    CLOTHING_TYPE_CHOICES = [
        ('classic', 'Classic'),
        ('casual', 'Casual'),
        ('sport', 'Sport'),
    ]
    SEASON_CHOICES = [
        ('spring', 'Spring'),
        ('summer', 'Summer'),
        ('fall', 'Fall'),
        ('winter', 'Winter'),
    ]

    age = models.CharField(max_length=10, choices=AGE_CHOICES)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    clothing_type = models.CharField(max_length=10, choices=CLOTHING_TYPE_CHOICES)
    season = models.CharField(max_length=10, choices=SEASON_CHOICES)
    image = models.ImageField(upload_to='media/clothes',)

    def __str__(self):
        return f"{self.age}, {self.gender}, {self.clothing_type}, {self.season}"