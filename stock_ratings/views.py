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
from polygon import RESTClient
from datetime import datetime, timedelta

@csrf_exempt
def stock_ratings(request):
    '''
    List all stock_rating snippets
    '''
    if(request.method == 'GET'):
        client = RESTClient("API_key_goes_here")
        tickers = ["AAPL", "MSFT", "AMZN"]
        datetime_now = datetime.now()
        first_date = datetime_now - timedelta(365)
        first_date_date = first_date.strftime('%Y-%m-%d')
        datetime_now_date = datetime_now.strftime('%Y-%m-%d')
        print(first_date_date, datetime_now_date)
        stocks_api_response = dict()
        stocks_api_response['labels'] = []
        stocks_api_response['datasets'] = dict()
        stocks_api_response['statistics'] = dict()
        for ticker in tickers:
            resp = client.stocks_equities_aggregates(ticker, 1, "day", first_date_date, datetime_now_date)
            print(resp.status)
            if resp.status == "OK" or resp.status == "DELAYED":
                stocks_api_response['datasets'][ticker] = dict()
                stocks_api_response['statistics'][ticker] = dict()
                stocks_api_response['datasets'][ticker]['vw_values_dataset'] = []
                for result in resp.results:
                    if "t" in result:
                        timestam_ms = float(result['t'])/1000.0
                        date_t = datetime.fromtimestamp(timestam_ms).strftime('%Y-%m-%d')
                        print(date_t, result['vw'])
                        stocks_api_response['datasets'][ticker]['vw_values_dataset'].append(result['vw'])
                        if date_t not in stocks_api_response['labels']:
                            stocks_api_response['labels'].append(date_t)
                statistics = StockRating.getStockStatistics(stocks_api_response['datasets'][ticker]['vw_values_dataset'])
                stocks_api_response['statistics'][ticker]['ticker_symbol'] = ticker
                stocks_api_response['statistics'][ticker]['cumulative_return'] = statistics['cumulative_return']
                stocks_api_response['statistics'][ticker]['annualized_return'] = statistics['annualized_return']
                stocks_api_response['statistics'][ticker]['annualized_volatility'] = statistics['annualized_volatility']
            else:
                print("Status not OK or DELAYED")
        # get all the stock_ratings
        return JsonResponse(stocks_api_response,safe=False)
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
    
# @csrf_exempt
# def stock_rating_detail(request, pk):
#     try:
#         # obtain the stock_rating with the passed id.
#         stock_rating = StockRating.objects.get(pk=pk)
#     except:
#         # respond with a 404 error message
#         return HttpResponse(status=404)  
#     if(request.method == 'PUT'):
#         # parse the incoming information
#         data = JSONParser().parse(request)  
#         # instanciate with the serializer
#         serializer = StockRatingSerializer(stock_rating, data=data)
#         # check whether the sent information is okay
#         if(serializer.is_valid()):  
#             # if okay, save it on the database
#             serializer.save() 
#             # provide a JSON response with the data that was submitted
#             return JsonResponse(serializer.data, status=201)
#         # provide a JSON response with the necessary error information
#         return JsonResponse(serializer.errors, status=400)
#     elif(request.method == 'DELETE'):
#         # delete the stock_rating
#         stock_rating.delete() 
#         # return a no content response.
#         return HttpResponse(status=204) 