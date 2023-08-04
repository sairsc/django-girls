from django import forms
from .models import Feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ("name", "email", "feedback")
        required_fields = ["name", "email", "feedback"]

    def clean_email(self):
        email = self.cleaned_data.get("email", "")
        if email.endswith("@softcatalyst.com"):
            return email
        raise forms.ValidationError("Invalid Domain")
