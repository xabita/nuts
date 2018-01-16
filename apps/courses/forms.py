
from django import forms
from .models import Course, CourseModule, Resource

# -----------------------------------------------------------------------------
# CONTENT FORMS
# -----------------------------------------------------------------------------
class CourseForm(forms.ModelForm):
	description = 	forms.CharField(
					widget=forms.Textarea(attrs={'class': 'form-control'}),
					label="Descripción",
				)
	class Meta:
		model = Course
		fields = ('name','description', 'usercourse',)

class CourseModuleForm(forms.ModelForm):
	description = 	forms.CharField(
					widget=forms.Textarea(attrs={'class': 'form-control'}),
					label="Descripción",)
	objective = 	forms.CharField(
					widget=forms.Textarea(attrs={'class': 'form-control'}),
					label="Objetivo del curso",
					)
	time = 	forms.CharField(
					widget=forms.TextInput(attrs={'class': 'form-control'}),
					label="Duración",
					)
	class Meta:
		model = CourseModule
		fields = ('name','description', 'objective', 'time', 'course',)


class ResourceForm(forms.ModelForm):
	
	class Meta:
		model = Resource
		fields = ('title','url_video', 'courseModule')

