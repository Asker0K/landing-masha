from django.shortcuts import render
from django.views import generic

# Create your views here.


class HomePageView(generic.TemplateView):

    template_name = 'landing/index.html'

    def get_context_data(self, **kwargs):
        context = {"landing_name": "Maria Portfolio"}
        return context
