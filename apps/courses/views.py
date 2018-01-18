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
		'title_page': 'Nuts'
	})

def new_course(request):
	index_template = "app/courses_new.html"
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
			course.save()
			return modules(request, course.id)
	else:
		return redirect('home')


def modules(request, pk):
	try:
		course = get_object_or_404(Course, pk=pk)
		list_courses = Course.objects.filter(pk=pk).order_by('-created_at')
		modules = CourseModule.objects.filter(course = course).order_by('-created_at')[:10]

		no_modules= len(modules)
		IdModule=course.id

		#coursesmodule_form = CourseModuleForm()


	except Course.DoesNotExist:
		raise Http404("Course does not exist")

	return render(request, 'app/modules.html', {
		'modules': modules,
		'list_courses': list_courses,
		'title_page': Course.name,
		'no_modules': no_modules,
		'IdModule': IdModule,
	})


def modules_new(request,pk):
	index_template = "app/modules_new.html"
	coursesmodule_form = CourseModuleForm()
	
	return render(request, index_template,{
		'title_page': 'Nuts',
		'form': coursesmodule_form,
		'idCourse': pk,
	})

def modules_add(request, pk):
	if request.method == "POST":
		form = CourseModuleForm(request.POST)
		if form.is_valid():
			course_module = form.save(commit=False)
			course_module.save()
			return resources(request, course_module.id)
	else:
		return redirect('home')

def resources(request, pk):
	try:
		module = get_object_or_404(CourseModule, pk=pk)
		list_module = CourseModule.objects.filter(pk=pk).order_by('-created_at')
		resources = Resource.objects.filter(courseModule = module).order_by('-created_at')[:10]
		resource_form = ResourceForm()

	except CourseModule.DoesNotExist:
		raise Http404("Course does not exist")

	return render(request, 'app/resources.html', {
		'resources': resources,
		'list_module': list_module,
		'form': resource_form,
	})

def new_resource(request, pk):
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








def resource_detail(request, pk):
	try:
		res = get_object_or_404(Resource, pk=pk)
		#list_module = CourseModule.objects.filter(pk=pk).order_by('-created_at')
		resources = Resource.objects.filter(pk = pk).order_by('-created_at')[:10]
		
	except CourseModule.DoesNotExist:
		raise Http404("Course does not exist")

	return render(request, 'app/resources_detail.html', {
		'resources': resources,
	})

