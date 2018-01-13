from __future__ import unicode_literals
from django.http import JsonResponse, HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from apps.courses.models import Course, CourseModule, Resource

from .forms import CourseForm, CourseModuleForm, ResourceForm

# Create your views here

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
			return course_detail(request, course.id)

			#return redirect('home')
	else:
		return redirect('home')


def new_course_module(request):
	index_template = "app/course_module.html"
	coursesmodule_form = CourseModuleForm()
	
	return render(request, index_template, {
		'title_page': 'Nuts',
		'form': coursesmodule_form,
	})

def add_course_module(request):
	if request.method == "POST":
		form = CourseModuleForm(request.POST)
		if form.is_valid():
			course_module = form.save(commit=False)
			course_module.save()
			return course_detail(request, course_module.course.pk)
	else:
		return redirect('home')



def new_resource(request):
	index_template = "app/resource.html"
	resource_form = ResourceForm()
	
	return render(request, index_template, {
		'title_page': 'Nuts',
		'form': resource_form,
	})

def add_resource(request):
	if request.method == "POST":
		form = ResourceForm(request.POST)
		if form.is_valid():
			resource = form.save(commit=False)
			#product_tmp = Product.objects.get(pk=request.POST.get("product",))
			#comment.product = product_tmp
			resource.save()
			return redirect('home')
	else:
		return redirect('home')

def course_detail(request, pk):
	try:
		course = get_object_or_404(Course, pk=pk)
		list_courses = Course.objects.filter(pk=pk).order_by('-created_at')
		modules = CourseModule.objects.filter(course = course).order_by('-created_at')[:10]
		coursesmodule_form = CourseModuleForm()


	except Course.DoesNotExist:
		raise Http404("Course does not exist")

	return render(request, 'app/course_detail.html', {
		'modules': modules,
		'list_courses': list_courses,
		'title_page': Course.name,
		'form': coursesmodule_form,
	})
