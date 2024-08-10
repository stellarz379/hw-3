from django.shortcuts import render
from apps.base.models import Setting, About
# Create your views here.
def index(request):
    setting_all = Setting.objects.all()
    about_all = About.objects.all()
    return render(request, "index.html", locals())