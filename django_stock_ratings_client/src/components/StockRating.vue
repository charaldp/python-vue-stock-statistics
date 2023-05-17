<template>
    <div class="stock_ratings_container">
        <div class="stock_ratings_content">
            <h1>Stock Ratings</h1>
            <div v-for="(stock_rating, key) in this.stock_ratings" :key="key">{{key}} {{stock_rating}}</div>
        </div>
        <div>
            <Line :data="data" :options="options" />
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
import * as chartConfig from './chartConfig.js'

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
            ...chartConfig,
            // stock_ratings
            stock_ratings: {}
        }
    },
    methods: {
        async getData() {
            try {
                // fetch stock_ratings
                const response = await axios.get('http://localhost:8000/api/stock_ratings/');
                // set the data returned as stock_ratings
                this.stock_ratings = response.data; 
            } catch (error) {
                // log the error
                console.log(error);
            }
        },
    },
    created() {
        // Fetch stock_ratings on page load
        this.getData();
    }
}
</script>