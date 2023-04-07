from django import forms
from .models import Todo

class AddNewTodoForm(forms.ModelForm):
    
    
    class Meta:
        model = Todo
        # fields = '__all__'
        fields = ['title', 'description','status']
        exclude = ['done', 'doned_at']
        
        widgets = {
            'title':forms.TextInput(attrs={"class":"form-control"}),
            'status':forms.Select(attrs={"class":"form-select"})
        }

    