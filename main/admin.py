from django.contrib import admin
from .models import MainCategory,Specialization,DoctorFullProfile
from tinymce.widgets import TinyMCE
from django.db import models


# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
	fieldsets = [
		("Title/date", {"fields": ["date_published","DateOfBirth","Phone_Number","Address"]}),
		("URL", {"fields":["doctor_slug"]}),
		("Speciality", {"fields":["speciality"]}),
		("Content", {"fields":["Full_name","Sex","Specialize","main_content","Google_Address"]}),
		("Images", {"fields":["CoverPhoto","ProfilePic"]}),
	]

	formfield_overrides = {
		models.TextField: {'widget': TinyMCE()},
		# models.CharField: {'widget': TinyMCE()}
	}

admin.site.register(MainCategory)
admin.site.register(Specialization)
admin.site.register(DoctorFullProfile, ArticleAdmin)
