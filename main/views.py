from django.shortcuts import render,redirect
from django.contrib import messages
from .models import MainCategory,Specialization,DoctorFullProfile



# Create your views here.
def homepage(request):
    return render(request=request,
                  template_name="main/categories.html",
                  context={"categories": MainCategory.objects.all})




def single_slug(request, single_slug):
    # first check to see if the url is in categories.

    categories = [c.cat_slug for c in MainCategory.objects.all()]
    if single_slug in categories:
        matching_series = Specialization.objects.filter(main_category__cat_slug=single_slug)
        series_urls = {}

        for m in matching_series.all():
            part_one = DoctorFullProfile.objects.filter(speciality__speciality=m.speciality).earliest("date_published")
            series_urls[m] = part_one.doctor_slug

        return render(request=request,
                      template_name='main/category.html',
                      context={"tutorial_series": matching_series, "part_ones": series_urls})

    doctorsDetails = [t.doctor_slug for t in DoctorFullProfile.objects.all()]

    if single_slug in doctorsDetails:
        this_doctor = DoctorFullProfile.objects.get(doctor_slug=single_slug)
        doctor_from_speciality = DoctorFullProfile.objects.filter(speciality__speciality=this_doctor.speciality).order_by('date_published')
        this_doctor_idx = list(doctor_from_speciality).index(this_doctor)

        return render(request=request,
                      template_name='main/articles.html',
                      context={"doctorsDetails": this_doctor,
                               "sidebar": doctor_from_speciality,
                               "this_doc_idx": this_doctor_idx})
    
