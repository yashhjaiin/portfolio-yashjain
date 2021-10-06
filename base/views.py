from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *

# Create your views here.
class Home(TemplateView):
    template_name = "base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data( **kwargs)

        context['about'] = About.objects.first()
        context['education'] = Education.objects.all()
        context['experience'] = Experience.objects.all()
        context['skill'] = Skill.objects.all()
        context['project'] = Project.objects.all()

        return context