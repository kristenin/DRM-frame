from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^books/$', views.BookListView.as_view(), name='books'),
    url(r'^books/(?P<pk>\d+)/$', views.BookDetailView.as_view(), name='info'),
]