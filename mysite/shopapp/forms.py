
from django import forms
class ProductForm(forms.Form):
    name = forms.CharField(label="Full name",max_length=100)
    price = forms.DecimalField(label="Price",min_value=0,max_value=1000000)
    description = forms.CharField(label="Description", widget=forms.Textarea(attrs={
        "rows": 5,
        "cols":30,
    }))