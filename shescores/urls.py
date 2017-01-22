"""shescores URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^soccer/', include('soccer.urls')),
    url(r'^$', RedirectView.as_view(url='/soccer/', permanent=True)),
]

# Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    url('^accounts/', include('django.contrib.auth.urls')),
]

"""
Django does not serve static files like CSS, JavaScript, and images by default, but it can be useful for the
development web server to do so while you're creating your site.
Uncomment the following line to do so.
"""
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
