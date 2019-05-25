from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^books/$', views.BookInfoViewSet.as_view({
        'get':'list',
        'post':'create'
    }), name='books-list'),
    url(r'^books/(?P<pk>\d+)/$', views.BookInfoViewSet.as_view({
        'get':'retrieve',
        'put':'update',
        'delete':'destroy'
    }), name='books-detail'),
    url(r'^books/latest/$', views.BookInfoViewSet.as_view({
        'get':'latest'
    }),name='books-latest'),
    url(r'^books/(?P<pk>\d+)/read/$', views.BookInfoViewSet.as_view({
        'put':'read'
    }), name='books-read')
]