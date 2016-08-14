from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('api.urls', namespace='api')),

    url(r'^$', views.IndexView.as_view(), name='index'),
    # url(r'^.*/$', views.IndexView.as_view()),
]
