from django import forms
from django.core import validators
class ProductForm(forms.Form):
    name = forms.CharField(max_length=100)
    price = forms.DecimalField(min_value=1,max_value=100000)
    description = forms.CharField(
        label="Description",
        widget=forms.Textarea(attrs={"rows":5,"cols":30}),
        validators=[validators.RegexValidator(
            regex=r"great",
            message="You need enter word <great>"
        )]
    )