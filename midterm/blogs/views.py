from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from online_shop.models import Category, Product
from online_shop.serializers import CategorySerializer, ProductSerializer
from django.views.decorators.csrf import csrf_exempt
import json



@csrf_exempt
def categories_handler(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return JsonResponse(serializer.data, status=200, safe=False)
    if request.method == 'POST':
        data = json.loads(request.body)
        serializer = CategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, status=200)
        return JsonResponse(data=serializer.errors, status=400)
    return JsonResponse({'message': 'Request is not supported'}, status=400)