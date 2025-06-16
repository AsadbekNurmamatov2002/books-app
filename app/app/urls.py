from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path("", include("books.urls")),
    path("user/", include("users.urls")),
    path('ckeditor/', include('ckeditor_uploader.urls')), 
    path('i18n/', include('django.conf.urls.i18n')), 
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT})
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.conf.urls.i18n import i18n_patterns

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
)