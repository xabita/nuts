from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from apps.users.models import UserCourse
from apps.courses.models import Course, CourseStudent
from .forms import UserCourseForm

# Create your views here

def home_users(request):
	index_template = "app/users_index.html"
	list_users = UserCourse.objects.filter().order_by('-user_type')
	
	return render(request, index_template, {
		'list_users': list_users,
		'title_page': 'Nuts'
	})


def users_new(request):
	index_template = "app/users_new.html"
	users_form = UserCourseForm()
	
	return render(request, index_template, {
		'title_page': 'Nuts.',
		'form': users_form,
	})

def users_add(request):
	if request.method == "POST":
		form = UserCourseForm(request.POST, request.FILES)
		if form.is_valid():
			us_course = form.save(commit=False)
			#us_course = UserCourse.objects.get(pk=usercourse_id)
			us_course.image = form.cleaned_data['image']
			us_course.save()

			pw = us_course.password
			us_course.set_password(pw)
			us_course.save()

		return home_users(request)
	else:
		return redirect('home')

def users_detail(request, pk):
	index_template = "app/users_detail.html"
	users_data = UserCourse.objects.get(pk=pk)
	if users_data.user_type==2:
		MyCourses = Course.objects.filter(usercourse=pk).order_by('-created_at')
	elif users_data.user_type==3:
		MyCourses = CourseStudent.objects.filter(user_student=pk).order_by('-created_at')
	else:
		MyCourses = Course.objects.filter(usercourse=pk).order_by('-created_at')


	
	return render(request, index_template, {
		'users_data': users_data,
		'MyCourses': MyCourses,
		'title_page': 'Nuts'
	})