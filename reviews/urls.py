from django.urls import path,include
from . import views
from rest_framework import routers

router= routers.DefaultRouter()
router.register('restaurants',views.RestaurantViewSet)
router.register('reviews',views.ReviewViewSet)

urlpatterns = [
    
     path('',include(router.urls)),
    
]


