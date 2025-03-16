<template>
    <v-container>
      <v-card max-width="400" class="mx-auto mt-5">
        <v-card-title>Sign Up</v-card-title>
        <v-card-text>
          <v-form @submit.prevent="handleSignup">
            <v-text-field v-model="username" label="Username" required></v-text-field>
            <v-text-field v-model="email" label="Email" required></v-text-field>
            <v-text-field v-model="password" label="Password" type="password" required></v-text-field>
            <v-btn type="submit" color="primary" block class="mt-2">Sign Up</v-btn>
          </v-form>
        </v-card-text>
      </v-card>
    </v-container>
  </template>
  
  <script>
  import { mapActions } from 'vuex'
  
  export default {
    name: 'SignupView',
    data() {
      return {
        username: '',
        email: '',
        password: ''
      }
    },
    methods: {
      ...mapActions(['signup']),
      async handleSignup() {
        try {
          await this.signup({ username: this.username, email: this.email, password: this.password })
          this.$router.push('/login')
        } catch (error) {
          console.error('Signup failed:', error)
          // Handle error (e.g., show error message)
        }
      }
    }
  }
  </script>
  