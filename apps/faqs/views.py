from django.shortcuts import redirect, render
from apps.faqs.models import ResourceComment
from apps.courses.models import Resource
from apps.users.models import UserCourse
from apps.faqs.forms import ResourceCommentForm

# Create your views here.
def add_comments(request, pk):
	if request.method == "POST":
		form = ResourceCommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			resource_tmp = Resource.objects.get(pk=pk)
			comment.resource = resource_tmp
			resource_us= request.POST.get('usercourse')
			resource_user = UserCourse.objects.get(pk=resource_us)
			comment.usercourse = resource_user
			comment.save()
			return redirect('resource_detail', resource_tmp.id)
	else:
		return redirect('contact')
