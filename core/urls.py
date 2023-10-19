from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from drf_yasg import openapi
from UZFI.views import Index

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description='''HEMIS Oliygoh tizimini boshqa axborot tizimlari bilan integratsiya qilish uchun API. So'rovlar uchun qaytadigan ma'lumotlar til parametri l berilmagan holatda o'zbek tilida qaytadi. 
      Kerakli tildagi natijalarni olish uchun mos til kodi so'rovga qo'shiladi, masalan: data/schedule-list?l=ru-RU so'rovida ma'lumotlar rus tilida qaytadi. 
      Til parametri uchun quyidagi qiymatlar mavjud:
      uz-UZ (o'zbek lotin)
      oz-UZ (o'zbek kirill)
      ru-RU (ruscha)
      en-US (inglizcha)
      ''',
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', Index.as_view()),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    # path('uzfi/', include('UZFI.urls')),
    # path('news/', include('News.urls')),

    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]+i18n_patterns (
    path('i18n/', include('django.conf.urls.i18n')),
    path('uzfi/', include('UZFI.urls')),
    path('news/', include('News.urls'))
)
# urlpatterns=[
#     *i18n_patterns(*urlpatterns, prefix_default_language=False),
#     ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
