from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.response import Response as rest_response, Response
from rest_framework.views import APIView

from .serializers import *
from .models import vehicleCategory, vehicle
from common.utils import create_message

# Create your views here.


class parentCategoryApi(APIView):
    def get(self, request, id= None):
        if id:
            parent_category_obj = vehicleCategory.objects.filter(id=id)
            serializer = getInventoryParentCategorySeializer(parent_category_obj, many=True)
            return rest_response(create_message(False, "Success", serializer.data))
        else:
            parent_category_obj = vehicleCategory.objects.all()
            serializer = getInventoryParentCategorySeializer(parent_category_obj,many=True)
            return rest_response(create_message(False, "Success", serializer.data))


    def post(self, request):
            serializer = getInventoryParentCategorySeializer.create(self,validated_data=request.data)
            if serializer:
                data = {'message': 'Successfully Added'}
                return rest_response(create_message(False, "Success", data))
            else:
                data = {'message': 'Error'}
                return rest_response(create_message(True, "Error", data))

    def patch(self, request, id=None):
        if id is None:
           return Response(create_message(True, "query_param_missing", []))
        request.data._mutable = True
        catgory = vehicleCategory.objects.get(id=id)
        serializer = getInventoryParentCategorySeializer(catgory, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(create_message(False, 'update_success', []))
        else:
            return Response(create_message(True, 'data_error_message', serializer.errors))


    def delete(self, request, id=None):
        if id is None:
            return Response(create_message(True, 'query_param_missing', []))
        vehicleCategory.objects.get(id=id).delete()
        return Response(create_message(False, 'success', []))


class vehicleApi(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, id= None):
        if id:
            parent_category_obj = vehicle.objects.filter(id=id)
            serializer = getInventoryCategorySeializer(parent_category_obj, many=True)
            return rest_response(create_message(False, "Success", serializer.data))
        else:
            parent_category_obj = vehicle.objects.all()
            serializer = getInventoryCategorySeializer(parent_category_obj,many=True)
            return rest_response(create_message(False, "Success", serializer.data))


    def post(self, request):
            serializer = InventoryCategorySeializer.create(self,validated_data=request.data)
            if serializer:
                data = {'message': 'Successfully Added'}
                return rest_response(create_message(False, "Success", data))
            else:
                data = {'message': 'Error'}
                return rest_response(create_message(True, "Error", data))

    def patch(self, request, id=None):
        if id is None:
           return Response(create_message(True, 'query_param_missing', []))
        request.data._mutable = True

        vehic = vehicle.objects.get(id=id)
        serializer = InventoryCategorySeializer(vehic, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(create_message(False, 'update_success', []))
        else:
            return Response(create_message(True, 'data_error_message', serializer.errors))


    def delete(self, request, id=None):
        if id is None:
            return Response(create_message(True, 'query_param_missing', []))
        vehicle.objects.get(id=id).delete()
        return Response(create_message(False, 'success', []))
