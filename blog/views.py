from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.


def homePage(request):
    return render(request, r"blog\index.html", {})


class HomeView(TemplateView):
    template_name = r'blog\index.html'


class AboutPage(TemplateView):
    template_name = r'blog\about.html'
