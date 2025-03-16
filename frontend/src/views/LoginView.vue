<template>
    <v-container>
      <v-card max-width="400" class="mx-auto mt-5">
        <v-card-title>Login</v-card-title>
        <v-card-text>
          <v-form @submit.prevent="handleLogin">
            <v-text-field v-model="email" label="Email" required></v-text-field>
            <v-text-field v-model="password" label="Password" type="password" required></v-text-field>
            <v-btn type="submit" color="primary" block class="mt-2">Login</v-btn>
          </v-form>
        </v-card-text>
      </v-card>
    </v-container>
  </template>
  
  <script>
  import { mapActions } from 'vuex'
  
  export default {
    name: 'LoginView',
    data() {
      return {
        email: '',
        password: ''
      }
    },
    methods: {
      ...mapActions(['login']),
      async handleLogin() {
        try {
          await this.login({ email: this.email, password: this.password })
          this.$router.push('/dashboard')
        } catch (error) {
          console.error('Login failed:', error)
          // Handle error (e.g., show error message)
        }
      }
    }
  }
  </script>
  