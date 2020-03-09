from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    url(r'', include('polls.urls')),
    #url(r'^accounts/', include('accounts.urls')),
    url('accounts/', include('django.contrib.auth.urls')),
    url(r'^sero/', include('sero.urls')),
    url(r'^socionetwork/', include('socionetwork.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),


]

if settings.DEBUG:
   urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)