from django.shortcuts import redirect, render
from apps.faqs.models import ResourceComment
from courses.models import Resource

from .forms import ResourceommentForm

# Create your views here.
def add_comments(request):
	if request.method == "POST":
		form = ResourceommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			resource_tmp = Resource.objects.get(pk=request.POST.get("resource",))
			comment.resource = resource_tmp
			comment.save()
			return redirect('resource_detail', resource_tmp.id)
	else:
		return redirect('contact')