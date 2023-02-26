from django.contrib import admin
from django.urls import path, include, re_path
from women.views import *
from rest_framework import routers

class MyCustomRouter(routers.SimpleRouter):
    routers = [
        routers.Route(
            url=r'^{prefix}$',
            mapping={'get': 'list'},
            name='{basename}-list',
            detail=False,
            initkwargs={'suffix': 'list'}),
        routers.Route(
            url=r'^{prefix}/{lookup}$',
            mapping={'get': 'retrieve'},
            name='{basename}-detail',
            detail=True,
            initkwargs={'suffix': 'Detail'})
    ]

router = MyCustomRouter()

router.register(r'women', WomenViewSet, basename='women')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/auth/', include('djoser.urls')),
    path('r^auth/', include('djoser.urls.authtoken')),

    # path('api/v1/womenlist/', WomenViewSet.as_view({'get':'list'})),
    # path('api/v1/womenlist/<int:pk>/',WomenViewSet.as_view({'put': 'update'})),
    # path('api/v1/womendetail/<int:pk>/',WomenAPIDetailView.as_view()),
]
