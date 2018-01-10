from __future__ import unicode_literals
from django.http import JsonResponse, HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from apps.courses.models import Course

# Create your views here.


def home(request):
	index_template = "app/index.html"
	list_courses = Course.objects.all().order_by('-created_at')

	return render(request, 'app/details_product.html', {
		'list_courses': list_courses,
		'title_page': 'Nuts.'
	})