from django.shortcuts import render

from .forms import ClothingForm
from .models import ClothingPreference


def clothing_form_view(request):
    if request.method == 'POST':
        form = ClothingForm(request.POST)
        if form.is_valid():
            age = form.cleaned_data['age']
            gender = form.cleaned_data['gender']
            clothing_type = form.cleaned_data['clothing_type']
            season = form.cleaned_data['season']
            clothing_preferences = ClothingPreference.objects.filter(
                age=age, gender=gender, clothing_type=clothing_type, season=season
            )
            return render(request, 'clothing_form_success.html', {
                'clothing_preferences': clothing_preferences,
            })
    else:
        form = ClothingForm()

    return render(request, 'index.html', {'form': form})
