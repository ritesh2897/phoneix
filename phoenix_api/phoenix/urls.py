from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from data.views import DataViewSet, SubscriberViewSet, PostViewSet
from identity.views import UserViewSet

router = routers.SimpleRouter()
router.register(r'data', DataViewSet)
router.register(r'subscriber', SubscriberViewSet)
router.register(r'post', PostViewSet)
router.register(r'user', UserViewSet)

urlpatterns = [
    path('phoenix/admin/', admin.site.urls),
    path('phoenix/api-auth/', include('rest_framework.urls')),
    path('phoenix/social/', include('social_django.urls', namespace='social')),
    path('phoenix/', include(router.urls))
]
