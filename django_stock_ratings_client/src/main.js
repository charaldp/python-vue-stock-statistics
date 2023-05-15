import { createApp } from 'vue'
import App from './App.vue'
// import Vue from 'vue'
var Vue = require('vue');

createApp(App).mount('#app')

// import axios
import axios from 'axios'

// set a prototype for http
Vue.prototype.$http = axios;