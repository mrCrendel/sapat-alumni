"""config URL Configuration

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
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.documentation import include_docs_urls

from config import settings


API_TITLE = '996 API DOCS'
API_DESCRIPTION = 'NO DESCRIPTION'

v1 = ([
    path('posts/', include('apps.posts.urls')),
], 'v1')


urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
    path('api/v1/', include(v1)),
]

if settings.DEBUG:
    urlpatterns += [
        path('docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)),
    ]

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)