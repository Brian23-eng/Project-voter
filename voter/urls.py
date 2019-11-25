from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers



router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('posts', views.PostViewSet)
router.register('profile', views.ProfileViewSet)

urlpatterns=[
    url('^$', views.home, name='home'),
    url(r'^api/', include(router.urls)),
    url(r'^(?P<username>\w+)/profile/', views.user_profile, name='userprofile'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^profile/(?P<username>\w+)',views.profile,name='profile'),
    url(r'^profile/(?P<username>\w+)/settings', views.edit_profile, name='edit'),
    url(r'^project/(?P<post>\w+)', views.project, name='project'),
    url(r'^search/', views.search_project, name='search'),
    url(r'^postImage/',views.post_image,name='postImage'),
]

