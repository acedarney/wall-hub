from django.urls import path
from .views import IndexView, ToDoView, WeatherView, CalendarView

urlpatterns = [
    path('', IndexView.as_view(), name='index-page'),
    path('todo', ToDoView.as_view(), name='todo-page'),
    path('weather', WeatherView.as_view(), name='weather-page'),
    path('calendar', CalendarView.as_view(), name='calendar-page')
]