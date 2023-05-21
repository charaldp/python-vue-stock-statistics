<template>
    <div class="stock_ratings_container">
        <div>
            <h1>Stock Ratings Graph</h1>
        </div>
        <div v-if="!throttled" class="chart-wrapper" style="width: 75%;align: center">
            <Line :data="chart_data" :options="chart_options" />
        </div>
        <div v-else>
            <p>Unable to Obtain Data. This is definately due to request throttling of the free stock API, the stock data will be available in 30 seconds or more</p>
        </div>
        <div>
            <h1>Stock Ratings Statistics</h1>
        </div>
        <div>
            <table>
                <tr>
                    <th v-for="(name, index) in statistics_data_names" :key="'name_'+index">
                        {{name}}
                    </th>
                </tr>
                <tr v-for="(ticker_data, ticker) in statistics_data"  :key="'ticker_'+ticker">
                    <td v-for="(value, statistic) in ticker_data" :key="'ticker_'+ticker+'_statistic_'+statistic">
                        {{value}}
                    </td>
                </tr>
            </table>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import {
    Chart as ChartJS,
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend
} from 'chart.js'
import { Line } from 'vue-chartjs'

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
)

export default {
    components: {
        Line
    },
    data() {
        return {
            chart_data: {
                labels: [],
                datasets: [
                    {
                        label: 'Data One',
                        backgroundColor: '#f87979',
                        data: []
                    }
                ]
            },
            line_colors: [
                '#002953',
                '#c7f464',
                '#ff6b6b',
                '#95d4f3',
                '#f1bb1b',
                '#003592',
                '#7c464f',
                '#ffb6b6',
                '#593f4d',
                '#1fb1bb',
            ],
            chart_options: {
                // aspectRatio: 2,
                responsive: true,
                maintainAspectRatio: true
            },
            stock_ratings: {},
            throttled: false,
            statistics_data: {
                'AAAA': {
                    ticker_symbol: "AAAA",
                    cumulative_return: "0.00",
                    annualized_return: "0.00",
                    annualized_volatility: "0.00",
                }
            },
            statistics_data_names: {
                ticker_symbol: "Ticker Symbol",
                cumulative_return: "Cumulative Return",
                annualized_return: "Annualized Return",
                annualized_volatility: "Annualized Volatility",
            }
        }
    },
    methods: {
        async getData() {
            try {
                // fetch stock_ratings
                const response = await axios.get('http://localhost:8000/api/stock_ratings/');
                // set the data returned as stock_ratings
                this.stock_ratings = response.data;
                this.updateChartData();
                this.updateStatisticsData();
                this.throttled = false;
            } catch (error) {
                // log the error
                console.log(error);
                this.throttled = true;
            }
        },
        updateChartData() {
            let chart_data = {labels: [], datasets: []};
            chart_data.labels = this.stock_ratings.labels;
            var i = 0;
            for(var dataset in this.stock_ratings.datasets) {
                chart_data.datasets.push({
                    label: dataset,
                    backgroundColor: this.line_colors[i],
                    data: this.stock_ratings.datasets[dataset].vw_values_dataset
                })
                i++;
                if (i >= this.line_colors.length) {
                    i = 0;
                }
            }
            this.chart_data = chart_data;
        },
        updateStatisticsData() {
            this.statistics_data = this.stock_ratings.statistics;
        },
    },
    created() {
        // Fetch stock_ratings on page load
        this.getData();
    }
}
</script>

<style>
table, th, td {
  border: 1px solid black;
  border-collapse: collapse;
}
#graph{
  position: relative;
  width: 80% !important;
}
</style>