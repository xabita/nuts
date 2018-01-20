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
			return home_users(request)
	else:
		return redirect('home')



