"""
URL configuration for formaspace project.

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
from django.contrib import admin
from django.urls import path, include
from core.views import home
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from core.sitemaps import StaticViewSitemap, BlogSitemap
from django.views.generic import TemplateView

sitemaps = {
    'static': StaticViewSitemap,
    'blog': BlogSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('branding/', include('branding.urls')),
    path('offices/', include('offices.urls')),
    path('', include('pages.urls')),   
    path('blog/', include('blog.urls')),
    path('enquiries/', include('enquiries.urls')),
    path('locations/', include('locations.urls')),
    path('integrations/', include('integrations.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path("privacy/", TemplateView.as_view(template_name="legal/privacy.html"), name="privacy"),
    path("terms/", TemplateView.as_view(template_name="legal/terms.html"), name="terms"),
    path("cookies/", TemplateView.as_view(template_name="legal/cookies.html"), name="cookies"),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



