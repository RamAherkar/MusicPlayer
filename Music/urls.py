from django.urls import path
from django.conf.urls import url

from . import views

app_name ='music'

urlpatterns = [
# 	path('music/'),		
    path('', views.IndexView.as_view(),name='index'),
    path('register/', views.UserFormView.as_view(),name='register'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name="detail"),
	path('album/add/',views.AlbumCreate.as_view(), name='album-add'),
	url(r'album/(?P<pk>[0-9]+)/$',views.AlbumUpdate.as_view(), name='album-update'),
	url(r'album/(?P<pk>[0-9]+)/delete/$',views.AlbumDelete.as_view(), name='album-delete'),

]
