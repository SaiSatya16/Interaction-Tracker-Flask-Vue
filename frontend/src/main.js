// In your main.js
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'

// Vuetify
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'
import { aliases, mdi } from 'vuetify/iconsets/mdi'
import '@mdi/font/css/materialdesignicons.css'

// v-network-graph
import VNetworkGraph from 'v-network-graph'
import 'v-network-graph/lib/style.css'

// Configure axios
axios.defaults.baseURL = 'http://localhost:5000/api'
const token = localStorage.getItem('token')
if (token) {
  axios.defaults.headers.common['Authorization'] = `Bearer ${token}`
}

const vuetify = createVuetify({
  components,
  directives,
  icons: {
    defaultSet: 'mdi',
    aliases,
    sets: {
      mdi,
    },
  },
  theme: {
    defaultTheme: localStorage.getItem('theme') || 'light',
    themes: {
      // Your theme configuration
    },
  },
})

createApp(App)
  .use(store)
  .use(router)
  .use(vuetify)
  .use(VNetworkGraph) // Add this line
  .mount('#app')
