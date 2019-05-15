from django import forms 
from funding.models import Category ,Project, Project_Image
class CreateProjectForm(forms.Form):
    title = forms.CharField(label='Title',max_length=100)
    details = forms.CharField(widget=forms.Textarea(attrs={"rows":4, "cols":50}))
    
    start_date = forms.DateField(label='Start Date')
    end_date = forms.DateField(label='End date')
    target= forms.FloatField(label='Target')
    category =forms.ModelChoiceField(label='Category', queryset = Category.objects.all())
    image = forms.ImageField(label='Image',required = False)   



class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')    
    class Meta:
        model = Project_Image
        fields = ('image' ,)    