from django.urls import path


from travels_app.views import (TravelCreateAV, TravelList,)


urlpatterns = [
    path('', TravelList.as_view(), name='travel-list'),
    path('create/', TravelCreateAV.as_view(), name='travel-create'),
]
