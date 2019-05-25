from rest_framework import status
from rest_framework import mixins
from rest_framework.viewsets import ViewSetMixin,ViewSet,GenericViewSet,ModelViewSet
from rest_framework.response import Response

from django.http import Http404
from booktest.models import BookInfo
from booktest.serializers import BookInfoSerializer

class BookInfoViewSet(ModelViewSet):
    serializer_class = BookInfoSerializer
    queryset = BookInfo.objects.all()

