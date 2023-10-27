from .models import Restaurant, Review
from rest_framework import viewsets
from .serializers import RestaurantSerializer,ReviewSerializer



#creating viewset for Restaurant and Review models

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset= Restaurant.objects.all()
    serializer_class= RestaurantSerializer
    
class ReviewViewSet(viewsets.ModelViewSet):
    queryset= Review.objects.all()
    serializer_class= ReviewSerializer
    

    


