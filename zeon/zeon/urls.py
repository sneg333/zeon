from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
<<<<<<< HEAD
    url(r'', include('polls.urls')),
    #url(r'', include('accounts.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')),
=======
    url(r'^admin/', admin.site.urls),
    url(r'', include('polls.urls')),
>>>>>>> bff963650052efeb23b401daf134fb717e539f90
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),

]

if settings.DEBUG:
   urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)