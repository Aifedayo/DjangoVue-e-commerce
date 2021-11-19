from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from product.urls import accounts_urlpatterns
from order.urls import accounts_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/vi/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
    path('api/v1/', include('product.urls')),
    path('api/v1/', include('order.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += accounts_urlpatterns
