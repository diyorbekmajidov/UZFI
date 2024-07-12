from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from UZFI.views import Index
# from django.conf.urls import url
from django.views.static import serve



urlpatterns = [
    path('uzfi/secretadmin', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    re_path('media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path('^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),


]+i18n_patterns (
    path('i18n/', include('django.conf.urls.i18n')),
    path('uzfi/', include('UZFI.urls')),
    path('news/', include('News.urls')),
    path('international/', include('International.urls')),
    path('', Index.as_view()),
    path('accounts/', include('django.contrib.auth.urls')),
)


# if settings.DEBUG:
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
