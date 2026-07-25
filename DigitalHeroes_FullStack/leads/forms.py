from django import forms

from .models import Lead


class LeadForm(forms.ModelForm):
    """ModelForm for collecting prospect leads from the landing page."""

    class Meta:
        model = Lead
        fields = ["name", "email", "budget", "message"]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter your full name",
                    "required": True,
                    "maxlength": 100,
                    "minlength": 2,
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter your email address",
                    "required": True,
                    "maxlength": 254,
                }
            ),
            "budget": forms.Select(
                attrs={
                    "class": "form-control",
                    "required": True,
                }
            ),
            "message": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                    "placeholder": "Tell us about your project goals",
                    "required": True,
                    "minlength": 10,
                    "maxlength": 1000,
                }
            ),
        }

    def clean_name(self):
        name = self.cleaned_data.get("name", "").strip()
        if len(name) < 2:
            raise forms.ValidationError("Please enter your full name.")
        return name

    def clean_message(self):
        message = self.cleaned_data.get("message", "").strip()
        if len(message) < 10:
            raise forms.ValidationError("Please provide at least 10 characters so we can understand your request.")
        return message
