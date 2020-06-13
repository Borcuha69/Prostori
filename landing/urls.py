from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contacts/$', views.contacts, name='contacts'),
    url(r'^baths/$', views.baths, name='baths'),
    url(r'^fermer/$', views.fermer, name='fermer'),
    url(r'^activity/$', views.activity, name='activity'),
    url(r'^fishing/$', views.fishing, name='fishing'),
    url(r'^horsewalking/$', views.horsewalking, name='horsewalking'),
    url(r'^zoo/$', views.zoo, name='zoo'),
]