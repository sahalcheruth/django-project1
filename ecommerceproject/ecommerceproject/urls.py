from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('shop.urls')),
    path('search/',include('search_app.urls')),
    path('cart/',include('cart.urls')),
    path('auth/', include('accounts.urls'))

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                         document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                         document_root=settings.MEDIA_ROOT)