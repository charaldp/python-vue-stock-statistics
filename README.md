# python-vue-stock-statistics

VueJS Front-End (Demo): Setting Up

Django Back-End (AWS-EC2): http://ec2-18-206-237-29.compute-1.amazonaws.com/api/stock_ratings/

Django Project for Exposing API for Viewing Stock Ratings Graph and Statistics

The Front-end (Vue 3) is separate from the Back-end (as a service) and it's code is in the folder ```./django_stock_ratings_client/```

The API called in the backend is ```<hostname>/api/stock_ratings/```

The Stocks API used in the backend is by https://polygon.io/

Packages Installed in pip environment (file requirements.txt for more detail):
* django
* polygon-api-client

Packages Installed via npm:
* vue-chart-js
