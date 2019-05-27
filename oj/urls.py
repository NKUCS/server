"""oj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path

urlpatterns = [
    url(r"^admin/", admin.site.urls),
    url(r"^api/", include("demo.urls.oj")),
    url(r"^teacher/lab/", include("lab.urls.admin")),
    url(r"^teacher/submission/", include("submission.urls.admin")),
    url(r"^api", include("lecture.urls.admin")),
    url(r"^administrator/role/", include("user.urls.admin")),
    url(r"^exam/student", include("exam.urls.admin")),
]
