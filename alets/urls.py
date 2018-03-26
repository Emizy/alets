from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from company import views

urlpatterns = [
                  url(r'^admin/', admin.site.urls),
                  url(r'^$', views.index, name="index"),
                  url(r'^contact/', views.contact, name="contact"),
                  url(r'^services/', views.services, name="services"),
                  url(r'^market/', views.market, name="market"),
                  url(r'^about/', views.about, name="about"),
                  # url(r'^detail/(?P<del_id>[0-9]+)/$', views.detail, name='detail'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
