from django import forms
from .models import ResourceComment

# -----------------------------------------------------------------------------
# CONTENT FORMS
# -----------------------------------------------------------------------------
class ResourceCommentForm(forms.ModelForm):
	comment = 	forms.CharField(
					widget=forms.Textarea(attrs={'class': 'form-control'}),
					label="Comentario",
				)

	class Meta:
		model = ResourceComment
		fields = ('comment',)

