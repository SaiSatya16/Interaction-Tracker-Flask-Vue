<template>
  <v-app :theme="theme">
    <v-app-bar app elevation="2">
      <v-app-bar-title class="font-weight-bold">Interaction Tracker</v-app-bar-title>
      
      <v-spacer></v-spacer>
      
      <div v-if="isAuthenticated">
        <v-btn to="/dashboard" text>Dashboard</v-btn>
        <v-btn to="/analytics" text>Analytics</v-btn>
      </div>
      
      <v-btn v-if="!isAuthenticated" to="/login" text>Login</v-btn>
      <v-btn v-if="!isAuthenticated" to="/signup" text>Sign Up</v-btn>
      
      <v-btn icon @click="toggleTheme" class="ml-2">
        <v-icon>{{ theme === 'dark' ? 'mdi-weather-sunny' : 'mdi-weather-night' }}</v-icon>
      </v-btn>
      
      <v-btn v-if="isAuthenticated" @click="logout" text class="ml-2">
        <v-icon left>mdi-logout</v-icon>
        Logout
      </v-btn>
    </v-app-bar>

    <v-main>
      <v-fade-transition mode="out-in">
        <router-view></router-view>
      </v-fade-transition>
    </v-main>
  </v-app>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'App',
  data() {
    return {
      theme: localStorage.getItem('theme') || 'light'
    }
  },
  computed: {
    ...mapGetters(['isAuthenticated'])
  },
  methods: {
    logout() {
      this.$router.push('/login')
      this.$store.dispatch('logout')
    },
    toggleTheme() {
      this.theme = this.theme === 'light' ? 'dark' : 'light'
      localStorage.setItem('theme', this.theme)
    }
  }
}
</script>

/* Add to your App.vue */
<style>
.v-fade-transition-enter-active,
.v-fade-transition-leave-active {
  transition: opacity 0.3s ease;
}

.v-fade-transition-enter-from,
.v-fade-transition-leave-to {
  opacity: 0;
}

.card-hover {
  transition: transform 0.2s, box-shadow 0.2s;
}

.card-hover:hover {
  transform: translateY(-5px);
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15) !important;
}

.list-item-transition-enter-active,
.list-item-transition-leave-active {
  transition: all 0.5s ease;
}

.list-item-transition-enter-from,
.list-item-transition-leave-to {
  opacity: 0;
  transform: translateX(-30px);
}
</style>

