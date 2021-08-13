from .models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core import serializers
import json


@api_view(['GET'])
def get_categories(request):
    categories = Catagory.objects.all()
    category_json = serializers.serialize('json', categories)
    return Response({'data': category_json})

@api_view(['GET'])
def get_products(request):
    products = Product.objects.all()
    products_json = serializers.serialize('json', products)
    return Response({'data': products_json})


# @api_view(['POST'])
# def create_categories(request):
    

#     name = ""
#     description = ""
#     if(request.body != None):
#         json_data_from_body =json.loads(request.body)
#         name = json_data_from_body['name']
#         description = json_data_from_body['description']

#     model_category = Catagory.objects.create(
#         name= name, description = description)
#     model_category.save()
#     model_json = serializers.serialize('json', [model_category])
#     return Response({'message': 'success creating catagories' 'data_created': model_json})

@api_view(['POST'])
def create_categories(request):
    name = ""
    description = ""

    if(request.body != None):
        json_data_from_body = json.loads(request.body)
        name = json_data_from_body['name']
        description = json_data_from_body['description']

    model_category = Catagory.objects.create(
        name=name, description=description)
    model_category.save()
    model_json = serializers.serialize('json', [model_category])

    return Response({'message': 'success creating categories', 'data_created': model_json})
