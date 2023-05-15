<template>
    <div class="stock_ratings_container">
        <div class="stock_ratings_content">
            <h1>Stock Ratings</h1>
            <!-- TODO Chart.js Stock Ratings -->
        </div>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                // stock_ratings
                stock_ratings: {}
            }
        },
        methods: {
            async getData() {
                try {
                    // fetch stock_ratings
                    const response = await this.$http.get('http://localhost:8000/api/stock_ratings/');
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