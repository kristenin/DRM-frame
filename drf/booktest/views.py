from django.http import JsonResponse, HttpResponse
from django.views import View

from booktest.models import BookInfo
import json

class BookListView(View):
    def get(self, request):
        books = BookInfo.objects.all()
        book_list = []
        for book in books:
            book_list.append({
                'id':book.id,
                'btitle':book.btitle,
                'bpub_date':book.bpub_date,
                'bread':book.bread,
                'bcomment':book.bcomment
            })
        return JsonResponse(book_list, safe=False)
    def post(self, request):
        req_data = request.body
        json_str = req_data.decode()
        req_dict = json.loads(json_str)

        book = BookInfo.objects.create(
            btitle=req_dict.get('btitle'),
            bpub_date = req_dict.get('bpub_date')
        )

        return JsonResponse({
            'id': book.id,
            'btitle': book.btitle,
            'bpub_date': book.bpub_date,
            'bread': book.bread,
            'bcomment': book.bcomment
        }, status=201)

class BookDetailView(View):
    def get(self, request,pk):
        try:
            book = BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist:
            return HttpResponse(status=404)

        return JsonResponse({
            'id': book.id,
            'btitle': book.btitle,
            'bpub_date': book.bpub_date,
            'bread': book.bread,
            'bcomment': book.bcomment
        })
    def put(self, request, pk):
        try:
            book = BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist:
            return HttpResponse(status=404)

        req_data = request.body
        json_str = req_data.decode()
        req_dict = json.loads(json_str)

        book.btitle = req_dict.get('btitle')
        book.bpub_date = req_dict.get('bpub_date')
        book.save()

        return JsonResponse({
            'id': book.id,
            'btitle': book.btitle,
            'bpub_date': book.bpub_date,
            'bread': book.bread,
            'bcomment': book.bcomment
        })

    def delete(self, request, pk):
        try:
            book = BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist:
            return HttpResponse(status=404)

        book.delete()

        return HttpResponse(status=204)