from django import forms

class CreateProjectForm(forms.Form):
    title = forms.CharField(label='Title',max_length=100)
    detials = forms.CharField(label='Details',max_length=1000)
    start_date = forms.DateField(label='Start Date')
    end_date = forms.DateField(label='End date')
    target= forms.FloatField(label='Target')
    category =forms.ChoiceField(label='Category')