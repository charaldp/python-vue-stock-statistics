<template>
  <div id="app">
    <StockRating />
  </div>
</template>
<script>
import StockRating from "./components/StockRating.vue";
export default {
  name: "App",
  components: {
    StockRating,
  },
};
</script>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>