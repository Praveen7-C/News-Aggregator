from django.urls import path
from news.views import scrape, news_list, statichome, weather_prediction, about
from django.views.generic import TemplateView # Import TemplateView

urlpatterns = [
    path('scrape/<str:name>/', scrape, name="scrape"),
    path('news/', news_list, name="home"),
    path('', statichome, name="breakinghome"),
    path('news/about.html', about, name="about"),
    path('home/', TemplateView.as_view(template_name='home.html'), name="home"),
    path('homestatic/', TemplateView.as_view(template_name='homestatic.html'), name="homestatic"),
    path('news/Weather_Prediction.html', weather_prediction, name="weather_prediction"),
]
