from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'

class ToDoView(TemplateView):
    template_name = 'todo.html'

class WeatherView(TemplateView):
    template_name = 'weather.html'

class CalendarView(TemplateView):
    template_name = 'calendar.html'