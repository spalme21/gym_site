from django import forms

class ChangeCreditsForm(forms.Form):
    """A form to add credits to a client."""
    credits_added = forms.IntegerField(min_value=0, initial=0, help_text="Enter the number of credits to add.")
