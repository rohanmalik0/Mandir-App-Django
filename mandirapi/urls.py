from django.urls import path
from .views import MandirListCreateView
urlpatterns = [
    path('api/mandir/', MandirListCreateView.as_view(),name='mandir-list-create'),
    
]
