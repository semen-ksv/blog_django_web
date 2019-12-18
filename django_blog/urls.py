
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views
from users.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/', include('users.urls')),
    path('blog/', include('my_blog.urls')),
    path('about/', views.about),
    path('', views.main_index, name='index_page'),
]

# Start Debug toolbar/ use only Debug = True
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
