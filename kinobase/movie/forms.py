from django import forms

class LoginForm(form.ModelForm):
    name = forms.TextField()
    age = forms.TextField()

    widgets = {
        "name":forms.TextInput(attrs={"class":"form-control", "id":"main"})
    }