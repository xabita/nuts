from django import forms
from .models import UserCourse

# -----------------------------------------------------------------------------
# CONTENT FORMS
# -----------------------------------------------------------------------------
class UserCourseForm(forms.ModelForm):
	first_name = 	forms.CharField(
					widget=forms.TextInput(attrs={'class': 'form-control'}),
					label="Nombre",
				)
	last_name = 	forms.CharField(
					widget=forms.TextInput(attrs={'class': 'form-control'}),
					label="Apellidos",
				)
	email = 	forms.CharField(
					widget=forms.TextInput(attrs={'class': 'form-control'}),
					label="Correo electrónico",
				)

	username = 	forms.CharField(
					widget=forms.TextInput(attrs={'class': 'form-control'}),
					label="Usuario",
				)
	password = 	forms.CharField(
					widget=forms.PasswordInput(attrs={'class': 'form-control'}),
					label="Contraseña",
				)
	image = forms.ImageField()

	class Meta:
		model = UserCourse
		fields = ('first_name','last_name', 'email', 'user_type', 'is_active', 'username','password', 'image')

	