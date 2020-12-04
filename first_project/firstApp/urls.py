from django.urls import path
from .views import index, form_name_view

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', index, name='home'),
    path('formpage/', form_name_view, name = 'form_name')
] + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)