from .models import ProductReviews
from django import forms

class ReviewForm(forms.ModelForm):
    class Meta:
        Model = ProductReviews
        fields = ['rate','feedback']

