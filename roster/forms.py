from django.forms import ModelForm

from .models import Client, ClassSession

from django.core.exceptions import ValidationError

class ChangeCreditsModelForm(ModelForm):
    """A form to add credits to a client."""
    def clean_credits(self):
        data = self.cleaned_data["credits"]

        if data < 0:
            raise ValidationError("Invalid amount - must not be less than zero")

    class Meta:
        model = Client
        fields = ["credits"]
        labels = {"credits": "Number of credits to add"}


class ScheduleClassModelForm(ModelForm):
    """A form to schedule a class session"""
    class Meta:
        model = ClassSession
        fields = ["class_type", "date_and_time", "roster"]