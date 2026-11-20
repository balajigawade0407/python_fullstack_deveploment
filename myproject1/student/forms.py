from django import forms


class Studentform_data(forms.Form):
    reg_no1 = forms.IntegerField(min_value=1)
    name1 = forms.CharField(max_length=20)
    email1 = forms.EmailField()
    marks1 = forms.IntegerField(required=False, min_value=0)
    dob1 = forms.DateField(required=False)