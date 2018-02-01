import os
import uuid
from django.conf import settings
from django.db import models

def make_upload_path(instance, filename):
	file_root, file_ext = os.path.splitext(filename)
	dir_name = '{module}/{model}'.format(module=instance._meta.app_label, model=instance._meta.model_name)
	file_root = str(uuid.uuid4())
	name = os.path.join(settings.MEDIA_ROOT, dir_name, file_root + file_ext.lower())

	# Delete existing file to overwrite it later
	if instance.pk:
		while os.path.exists(name):
			os.remove(name)

	return os.path.join(dir_name, file_root + file_ext.lower())