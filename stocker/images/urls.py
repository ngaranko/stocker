from django.conf.urls import url

from .views import ImagesView


urlpatterns = [
    url(r'^$', ImagesView.as_view()),
]