from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
<<<<<<< HEAD
    url(r'^accounts/', include('accounts.urls')),
    url(r'^sero/', include('sero.urls')),
    url(r'^admin/', admin.site.urls),
=======
    url(r'', include('polls.urls')),
    #url(r'', include('accounts.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
>>>>>>> 55aa9b47143832b2386e20a8c60c64f8ae032bea

    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    # url(r'', include('polls.urls')),
    # url(r'^accounts/', include('accounts.urls')),
]

if settings.DEBUG:
   urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)