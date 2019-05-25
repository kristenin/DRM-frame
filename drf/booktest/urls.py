from django.conf.urls import url
from . import views

urlpatterns = [
    
]

from rest_framework.routers import SimpleRouter,DefaultRouter
# router = SimpleRouter()
router = DefaultRouter()

router.register(r'books', views.BookInfoViewSet, base_name='books')
urlpatterns += router.urls