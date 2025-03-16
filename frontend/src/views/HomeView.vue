<template>
    <v-container>
      <h1>Welcome to Interaction Tracker</h1>
      <p>Track and analyze your daily interactions with ease.</p>
      <v-btn v-if="!isAuthenticated" to="/login" color="primary">Get Started</v-btn>
      <v-btn v-else to="/dashboard" color="primary">Go to Dashboard</v-btn>
    </v-container>
  </template>
  
  <script>
  import { mapGetters } from 'vuex'
  
  export default {
    name: 'HomeView',
    computed: {
      ...mapGetters(['isAuthenticated'])
    }
  }
  </script>
  