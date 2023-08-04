from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import SimpleRouter
from .views import UserCreation

router = SimpleRouter()

router.register('register',UserCreation,basename='user-create')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/',include(router.urls))
]
