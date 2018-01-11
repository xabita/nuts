
from django import forms
from .models import Course

# -----------------------------------------------------------------------------
# CONTENT FORMS
# -----------------------------------------------------------------------------
class CourseForm(forms.ModelForm):
	'''comment = 	forms.CharField(
					widget=forms.Textarea(attrs={'class': 'form-control'}),
					label="Comentario",
				)'''

	class Meta:
		model = Course
		fields = ('name','description', 'usercourse',)

