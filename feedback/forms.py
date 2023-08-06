from django import forms
from .models import Feedback
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Div, HTML


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ("name", "email", "feedback")
        required_fields = ["name", "email", "feedback"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column("name", css_class="col-md-6 mb-0"),
                Column("email", css_class="col-md-6 mb-0"),
                css_class="row col-md-12",
            ),
            Row(
                Column("feedback", css_class="form-group col-md-12 mb-2"),
                css_class="row",
            ),
            Div(
                HTML(
                    '<button type="submit" class="save btn btn-secondary">Save</button>'
                )
            ),
        )

    def clean_email(self):
        email = self.cleaned_data.get("email", "")
        if email.endswith("@softcatalyst.com"):
            return email
        raise forms.ValidationError(
            "Email is invalid. The email should be a softcatalyst email"
        )
