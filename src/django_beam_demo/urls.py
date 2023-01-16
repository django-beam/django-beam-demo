"""django_beam_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from beam.contrib.auth.views import UserViewSet, GroupViewSet
from beam.views import DashboardView
from customers.views import OrganizationViewSet, PersonViewSet
from projects.views import ProjectViewSet

urlpatterns = [
    path("", DashboardView.as_view(), name="dashboard"),
    path("organization/", include(OrganizationViewSet().get_urls())),
    path("person/", include(PersonViewSet().get_urls())),
    path("project/", include(ProjectViewSet().get_urls())),
    path("accounts/", include("django.contrib.auth.urls")),
    path("auth/", include("beam.contrib.auth.urls")),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
