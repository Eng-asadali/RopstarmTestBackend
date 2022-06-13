
from django.urls import path
from .views import parentCategoryApi, vehicleApi

urlpatterns = [
    path('vehicleCategory/', parentCategoryApi.as_view()),
    path('vehicleCategory/delete/<int:id>/', parentCategoryApi.as_view()),
    path('vehicleCategory/details/<int:id>/', parentCategoryApi.as_view()),
    path('vehicle/', vehicleApi.as_view()),
    path('vehicle/delete/<int:id>/', vehicleApi.as_view()),
    path('vehicle/details/<int:id>/', vehicleApi.as_view()),
]