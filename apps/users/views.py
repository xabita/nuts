from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from apps.users.models import UserCourse

from .forms import UserCourseForm

# Create your views here

def home_users(request):
	index_template = "app/users_index.html"
	list_users = UserCourse.objects.all().order_by('-created_at')
	
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
		form = UserCourseForm(request.POST)
		if form.is_valid():
			us_course = form.save(commit=False)
			us_course.save()
			pw = us_course.password
			us_course.set_password(pw)
			us_course.save()

			#if "session_estatus" not in request.session:
				
			#	request.session['user_cur'] = user_data.first_name + ' ' + user_data.last_name
			#	request.session['session_estatus'] = user_data.is_active
			#	request.session['user_type'] = user_data.user_type
			#	request.session['id'] = user_data.id

		return home_users(request)
	else:
		return redirect('home')


def logoutUs(request):


	index_template = "app/index.html"
	
	if "session_estatus" in request.session:
		request.session['user_cur'] = ''
		request.session['session_estatus'] = False
		request.session['user_type'] = 0
		request.session['id'] = 0

	
	return render(request, index_template, {
		'title_page': 'Nuts.',
	})

