from django import forms

class ClothingForm(forms.Form):
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

    age = forms.ChoiceField(choices=AGE_CHOICES, widget=forms.RadioSelect)
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
    clothing_type = forms.ChoiceField(choices=CLOTHING_TYPE_CHOICES, widget=forms.RadioSelect)
    season = forms.ChoiceField(choices=SEASON_CHOICES, widget=forms.RadioSelect)
