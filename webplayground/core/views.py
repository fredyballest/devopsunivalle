from django.views.generic.base import TemplateView
from django.shortcuts import render

class HomePageView(TemplateView):
    template_name = "core/home.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'title':"Mi UNo Super Web Playground Edit1"})

class SamplePageView(TemplateView):
    template_name = "core/sample.html"
