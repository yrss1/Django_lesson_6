from django.urls import path
from .views import getTours,getReviews,getTourists,getTourByName
urlpatterns = [
    path('tours/', getTours),
    path('reviews/', getReviews),
    path('tourists/', getTourists),
    path('tour/<str:name>', getTourByName),
]
