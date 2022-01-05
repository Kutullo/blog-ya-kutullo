
from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from  django.conf.urls.static import  static

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('home/',include('home.urls')),
    path ('',include('home.urls')),
    path ('articles/',include('article.urls')),
    path ('user/',include('django.contrib.auth.urls')),
    path ('user/',include('accounts.urls')),




] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

