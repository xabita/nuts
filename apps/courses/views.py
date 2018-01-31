from __future__ import unicode_literals
from django.http import JsonResponse, HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from apps.courses.models import Course, CourseModule, Resource
from apps.users.models import UserCourse
from .forms import CourseForm, CourseModuleForm, ResourceForm, CourseStudentForm


from apps.faqs.forms import ResourceCommentForm
from apps.faqs.models import ResourceComment



# Create your views here
def home(request):
	index_template = "app/index.html"
	list_courses = Course.objects.all().order_by('-created_at')
	user_data = UserCourse.objects.get(pk=1)
	
	return render(request, index_template, {
		'list_courses': list_courses,
		'user_data': user_data,
		'title_page': 'Nuts'
	})

def new_course(request):
	index_template = "app/courses_new.html"
	courses_form = CourseForm()
	c_users = UserCourse.objects.filter(user_type=2).order_by('first_name')
    
	
	return render(request, index_template, {
		'title_page': 'Nuts.',
		'form': courses_form,
		'c_users': c_users,
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


def my_courses(request, pk):
	index_template = "app/courses_for_teacher.html"
	list_courses = Course.objects.filter(usercourse=pk).order_by('-created_at')
	user_data = UserCourse.objects.get(pk=pk)
	
	return render(request, index_template, {
		'list_courses': list_courses,
		'user_data': user_data,
		'title_page': 'Nuts'
	})

def modules(request, pk):
	try:
		course = get_object_or_404(Course, pk=pk)
		list_courses = Course.objects.filter(pk=pk).order_by('-created_at')
		modules = CourseModule.objects.filter(course = course).order_by('-created_at')[:10]
		no_modules= len(modules)
		IdCourse=course.id
		courseStudent_form = CourseStudentForm()

	
	except Course.DoesNotExist:
		raise Http404("Course does not exist")

	return render(request, 'app/modules.html', {
		'modules': modules,
		'list_courses': list_courses,
		'title_page': Course.name,
		'no_modules': no_modules,
		'IdCourse': IdCourse,
		'formStudent': courseStudent_form,
		
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
		course = Course.objects.get(pk=pk)
		if form.is_valid():
			course_module = form.save(commit=False)
			course_module.save()
			course_module.course=course
			course_module.save()
			return resources(request, course_module.id)
	else:
		return redirect('home')

def resources(request, pk):
	try:
		module = get_object_or_404(CourseModule, pk=pk)
		list_module = CourseModule.objects.filter(pk=pk).order_by('-created_at')
		resources = Resource.objects.filter(courseModule = module).order_by('-created_at')[:10]
		no_resources= len(resources)
		IdModule=module.id
		
		resource_form = ResourceForm()

	except CourseModule.DoesNotExist:
		raise Http404("Course does not exist")

	return render(request, 'app/resources.html', {
		'resources': resources,
		'list_module': list_module,
		'form': resource_form,
		'no_resources': no_resources,
		'IdModule': IdModule,
	})

def resource_new(request, pk):
	index_template = "app/resources_new.html"
	resource_form = ResourceForm()
	
	return render(request, index_template, {
		'title_page': 'Nuts',
		'form': resource_form,
		'IdModule': pk,
	})

def resource_add(request,pk):
	if request.method == "POST":
		form = ResourceForm(request.POST)
		module = CourseModule.objects.get(pk=pk)
		if form.is_valid():
			resource = form.save(commit=False)
			resource.save()
			resource.courseModule=module
			resource.save()
			return resource_detail(request, resource.id)
	else:
		return redirect('home')

def resource_detail(request, pk):
	try:
		res = get_object_or_404(Resource, pk=pk)
		#list_module = CourseModule.objects.filter(pk=pk).order_by('-created_at')
		resources = Resource.objects.filter(pk = pk).order_by('-created_at')[:10]
		Urlvideo=res
		comments = ResourceComment.objects.filter(resource = res).order_by('-created_at')[:10]
		comment_form = ResourceCommentForm()
	

		
	except CourseModule.DoesNotExist:
		raise Http404("Course does not exist")

	return render(request, 'app/resources_detail.html', {
		'resources': resources,
		'Urlvideo': Urlvideo,
		'form': comment_form,
		'comments': comments,
		
	})

def student_new(request):
	index_template = "app/student_new.html"
	courseStudent_form = CourseStudentForm()
	
	return render(request, index_template, {
		'title_page': 'Nuts.',
		'formS': courseStudent_form,
	})

def student_add(request, studentId, courseId):
	print(studentId)
	if request.method == "POST":
		form = CourseStudentForm(request.POST)
		student = CourseStudent.objects.get(pk=studentId)
		course = Course.objects.get(pk=courseId)

		if form.is_valid():
			CourseStudent = form.save(commit=False)
			CourseStudent.save()
			CourseStudent.user_student= student
			CourseStudent.course= course
			CourseStudent.save()


			return modules(request, CourseStudent.course)
	else:
		return redirect('home')
