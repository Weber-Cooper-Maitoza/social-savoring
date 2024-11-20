"""
URL configuration for socialSavoring project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from recipies import views as recipie_views
from profiles import views as profile_views
from socialMedia import views as socialMedia_views
from django.contrib.auth import views as authentication_views
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', authentication_views.LoginView.as_view(template_name='profiles/login.html'), name="login"),
    path('logout/', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
    path('social/', include("socialMedia.urls")),
    path('profile/', include("profiles.urls")),

    path('admin/', admin.site.urls),
]
urlpatterns += [] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)