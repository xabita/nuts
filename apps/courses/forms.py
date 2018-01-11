
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


class CourseModuleForm(forms.ModelForm):
	
	class Meta:
		model = CourseModule
		fields = ('name','description', 'objective', 'time', 'course',)


class ResourceForm(forms.ModelForm):
	
	class Meta:
		model = Resource
		fields = ('title','url_video', 'courseModule', 'description',)