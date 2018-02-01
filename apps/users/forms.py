from django import forms
from .models import UserCourse

# -----------------------------------------------------------------------------
# CONTENT FORMS
# -----------------------------------------------------------------------------
class UserCourseForm(forms.ModelForm):
	image = forms.ImageField()

	class Meta:
		model = UserCourse
		fields = ('first_name','last_name', 'email', 'user_type', 'is_active', 'username','password', 'image')
