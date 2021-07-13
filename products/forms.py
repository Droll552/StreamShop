from django import forms

from .models import MediaProduct


class MediaForm(forms.ModelForm):

    class Meta:
        model = MediaProduct
        exclude = [
            "user",
            "created_at",
            "product_type",
        ]
