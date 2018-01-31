
from django import forms
from .models import Course, CourseModule, Resource, CourseStudent, UserCourse

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

		def __init__(self, *args, **kwargs):
			super().__init__(*args, **kwargs)
			self.fields['usercourse'].queryset = UserCourse.objects.none()


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
		fields = ('name','description', 'objective', 'time' )
	
class ResourceForm(forms.ModelForm):
	content = forms.CharField (widget = AdminPagedownWidget ()) ,
	
	class Meta:
		model = Resource
		fields = ('title','url_video', 'content', 'category', )

class CourseStudentForm(forms.ModelForm):
	class Meta:
		model = CourseStudent
		fields = ('is_active',)


