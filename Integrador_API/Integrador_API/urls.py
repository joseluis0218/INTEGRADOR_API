
from django.conf.urls import url,include
from django.contrib import admin
admin.autodiscover()
from django.urls import path
from rest_framework import routers
from rest.views import UsuarioViewSet, CapturaViewSet,RostroViewSet

router = routers.DefaultRouter()
router.register(r'usuarios',UsuarioViewSet)
router.register(r'capturas',CapturaViewSet)
router.register(r'rostros',CapturaViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/', include(router.urls))
]
