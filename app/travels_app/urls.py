from django.urls import path
from travels_app.views import CategoryCreateAV, CategoryDetailAV


from travels_app.views import (TravelCreateAV, TravelList,CategoryList, CategoryDetailAV)


urlpatterns = [
    path('', TravelList.as_view(), name='travel-list'),
    path('create/', TravelCreateAV.as_view(), name='travel-create'),
    path('categories/', CategoryList.as_view(),name='category-list'),
    path('categories/create/', CategoryCreateAV.as_view(),name='category-create'),
    path('category/<int:pk>/', CategoryDetailAV.as_view(),name='category-detail')
]


