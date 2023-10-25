from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from UZFI.views import Index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]+i18n_patterns (
    path('i18n/', include('django.conf.urls.i18n')),
    path('uzfi/', include('UZFI.urls')),
    path('news/', include('News.urls')),
    path('', Index.as_view()),
    path('accounts/', include('django.contrib.auth.urls')),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
