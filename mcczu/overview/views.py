from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class IndexView(TemplateView):
    template_name = 'overview/index.html'


class RegisterView(TemplateView):
    template_name = 'overview/regist.html'

class MainpageView(TemplateView):
    template_name = 'overview/mainpage.html'