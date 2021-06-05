from django import forms
from .models import Comment

class AddCommentForm(forms.ModelForm):
	# Add Comment 
	class Meta:
		model = Comment
		fields = '__all__' # Hamma maydonini olish
		exclude = ['post'] # qaysi maydonlarni korsatmaslik
		# fields = ['name', 'email','subject', 'comment'] 