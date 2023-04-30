from django import forms

class RegionForm(forms.Form):
    region_name = forms.CharField(label='Region Name', max_length=100)
    text = forms.CharField(label='Text', max_length=1000, widget=forms.Textarea)

    