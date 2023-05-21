from django.db import models
from math import sqrt

# Create your models here.
class StockRating(models.Model):
    #title
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True) #description
    value = models.FloatField()
    #completed
    created_at = models.DateTimeField(auto_now_add=True) #created_at

    def __str__(self):
        #return the stock rating title
        return self.title
    
    def getStockStatistics(timeseries_data):
        statistics = dict()
        # Use two last elements for the current daily cumulative return
        # Use two last element and the value at the start of the year for the current annual cumulative return
        # (annual is considered as in the current year, and not in a 12 month range)
        trading_days = len(timeseries_data)
        if trading_days <= 1:
            statistics['cumulative_return'] = 0.00
            statistics['annualized_return'] = 0.00
            statistics['annualized_volatility'] = 0.00
            return statistics
        daily_returns = []
        sum_daily_return = 0
        for i in range(1, trading_days):
            daily_return = 100 * (timeseries_data[i] - timeseries_data[i-1]) / timeseries_data[i-1]
            daily_returns.append(daily_return)
            sum_daily_return += daily_return
        average_daily_return = sum_daily_return / trading_days
        sum_std = 0
        for j in range(trading_days - 1):
            sum_std += pow(daily_returns[j] - average_daily_return, 2)
        daily_volatility = sqrt(sum_std / trading_days)
        statistics['annualized_volatility'] = '{:.2f}'.format(daily_volatility * trading_days)
        statistics['cumulative_return'] = '{:.2f}'.format(daily_returns[-1])
        statistics['annualized_return'] = '{:.2f}'.format(100 * (timeseries_data[-1] - timeseries_data[0]) / timeseries_data[0])
        return statistics

    