from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Home, TitleSection, Section, Hystories, Statistics, AboutUs, UpcomingEvents


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        # Llamar al contexto original
        context = super().get_context_data(**kwargs)
        
        # Obtener los posts y los comentarios
        home = Home.objects.all()
        titleSection = TitleSection.objects.first()
        section = Section.objects.all()
        hystories = Hystories.objects.all()
        statistics = Statistics.objects.all()
        aboutUs = AboutUs.objects.all()
        upcomingEvents = UpcomingEvents.objects.all()

        # Pasar los objetos al contexto
        context['home'] = home
        context['titleSection'] = titleSection
        context['section'] = section
        context['hystories'] = hystories
        context['statistics'] = statistics
        context['aboutUs'] = aboutUs
        context['upcomingEvents'] = upcomingEvents
        return context