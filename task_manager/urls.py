"""
URL configuration for task_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.views.generic import TemplateView
from rest_framework import permissions
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path('api_schema/', get_schema_view(
        title="TASK MANAGER API",
        public=True,
        permission_classes=(permissions.AllowAny,)
    ), name='api_schema'),
    path('swagger-ui/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url':'api_schema'}
        ), name='swagger-ui'),
    path('admin/', admin.site.urls),
    path('api/', include('task_manager_app.urls')),
    path('api/auth/', include('auth.urls')),
]
