from django import forms
from django.core.exceptions import ValidationError

from livestreams.models import Livestream

from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput


class LivestreamCreateForm(forms.ModelForm):
    class Meta:
        model = Livestream
        exclude = [
            "user",
            "status"
        ]

        widgets = {
            "date": DatePickerInput(),
            "time": TimePickerInput(),
        }

    def clean_tags(self):
        tags = self.cleaned_data.get('tags')
        if len(tags) > 8:
            raise ValidationError('Maximum number of tags is 8', code='invalid')
        return tags


class LivestreamUpdateForm(forms.ModelForm):
    class Meta:
        model = Livestream
        exclude = [
            "user"
        ]
