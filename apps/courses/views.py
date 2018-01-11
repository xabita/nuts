from __future__ import unicode_literals
from django.http import JsonResponse, HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from apps.courses.models import Course

from .forms import CourseForm

# Create your views here.


def home(request):
	index_template = "app/index.html"
	list_courses = Course.objects.all().order_by('-created_at')
	
	return render(request, index_template, {
		'list_courses': list_courses,
		'title_page': 'Nuts.'
	})


def new_course(request):
	index_template = "app/courses.html"
	courses_form = CourseForm()
	
	return render(request, index_template, {
		'title_page': 'Nuts.',
		'form': courses_form,
	})




def add_courses(request):
	if request.method == "POST":
		form = CourseForm(request.POST)
		if form.is_valid():
			course = form.save(commit=False)
			#product_tmp = Product.objects.get(pk=request.POST.get("product",))
			#comment.product = product_tmp
			course.save()
			return redirect('home')
	else:
		return redirect('home')

 