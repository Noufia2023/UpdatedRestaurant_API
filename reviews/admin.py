from django.contrib import admin
from .models import Restaurant,Review


#admin.site.register(Restaurant)
#admin.site.register(Review)

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display=('name','address','average_rating')
    search_fields=('name',) #searching the field using restaurant's name

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display=('restaurant','rating','comment')
    search_fields=('restaurant__name',) #searching the field using restaurant's name

   


