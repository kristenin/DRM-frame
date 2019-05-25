from django.http import Http404
from rest_framework import status
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, ViewSetMixin, GenericViewSet, ModelViewSet

from booktest.models import BookInfo
from booktest.serializers import BookInfoSerializer

class BookInfoViewSet(ModelViewSet):
    serializer_class = BookInfoSerializer
    queryset = BookInfo.objects.all()

    def latest(self, request):
        book = BookInfo.objects.latest('id')
        serializer = self.get_serializer(book)
        return Response(serializer.data)

    def read(self, request, pk):
        book = self.get_object()
        bread = request.data.get('bread')
        if not bread:
            return Response({'code':'缺少bread参数'}, status=status.HTTP_400_BAD_REQUEST)
        book.bread = bread
        book.save()
        serializer = self.get_serializer(book)
        return Response(serializer.data)