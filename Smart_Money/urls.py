"""
URL configuration for Smart_Money project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.auth import views
from django.contrib import admin
from django.urls import path, include
from userextend.forms import AuthenticationNewForm
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
   path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('',include('finances.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('login/', views.LoginView.as_view(template_name='registrations/login.html',form_class=AuthenticationNewForm) , name='login'),
    path('', include('django.contrib.auth.urls')),
    path('',include('userextend.urls')),
    path('investing/',include('investing.urls')),


]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)