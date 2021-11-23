from django.forms import ModelForm
from .models import Comment
from django.forms.widgets import TextInput, Textarea

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        # fields = ["name", "message"]
        fields = "__all__" #Shu modelni hamma maydoni uchun form hosil qilish
        exclude = ["post"]
        widgets = {
            "name":TextInput(attrs={'class':'input',"data-color":'red'}),
            "message":Textarea(
                attrs={
                'class':'textarea',
                "rows":2,
                "cols":50}
            )

        }