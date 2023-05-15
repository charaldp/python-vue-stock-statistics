from django.shortcuts import render
# parsing data from the client
from rest_framework.parsers import JSONParser
# To bypass having a CSRF token
from django.views.decorators.csrf import csrf_exempt
# for sending response to the client
from django.http import HttpResponse, JsonResponse
# API definition for stock_rating
from .serializers import StockRatingSerializer
# StockRating model
from .models import StockRating

@csrf_exempt
def stock_ratings(request):
    '''
    List all stock_rating snippets
    '''
    if(request.method == 'GET'):
        # get all the stock_ratings
        stock_ratings = StockRating.objects.all()
        # serialize the stock_rating data
        serializer = StockRatingSerializer(stock_ratings, many=True)
        # return a Json response
        return JsonResponse(serializer.data,safe=False)
    elif(request.method == 'POST'):
        # parse the incoming information
        data = JSONParser().parse(request)
        # instanciate with the serializer
        serializer = StockRatingSerializer(data=data)
        # check if the sent information is okay
        if(serializer.is_valid()):
            # if okay, save it on the database
            serializer.save()
            # provide a Json Response with the data that was saved
            return JsonResponse(serializer.data, status=201)
            # provide a Json Response with the necessary error information
        return JsonResponse(serializer.errors, status=400)
    
@csrf_exempt
def stock_rating_detail(request, pk):
    try:
        # obtain the stock_rating with the passed id.
        stock_rating = StockRating.objects.get(pk=pk)
    except:
        # respond with a 404 error message
        return HttpResponse(status=404)  
    if(request.method == 'PUT'):
        # parse the incoming information
        data = JSONParser().parse(request)  
        # instanciate with the serializer
        serializer = StockRatingSerializer(stock_rating, data=data)
        # check whether the sent information is okay
        if(serializer.is_valid()):  
            # if okay, save it on the database
            serializer.save() 
            # provide a JSON response with the data that was submitted
            return JsonResponse(serializer.data, status=201)
        # provide a JSON response with the necessary error information
        return JsonResponse(serializer.errors, status=400)
    elif(request.method == 'DELETE'):
        # delete the stock_rating
        stock_rating.delete() 
        # return a no content response.
        return HttpResponse(status=204) 