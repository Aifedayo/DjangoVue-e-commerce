from django.urls import path, include

from order import views

urlpatterns = [
    path('checkout/', views.checkout)
]

accounts_urlpatterns = [
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
]