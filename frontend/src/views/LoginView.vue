<!-- frontend/src/views/LoginView.vue -->
<template>
  <v-container class="fill-height" fluid>
    <v-row align="center" justify="center">
      <v-col cols="12" sm="8" md="6" lg="4">
        <v-card elevation="4" rounded="lg" class="pa-4">
          <v-card-title class="text-h4 font-weight-bold text-center mb-4">
            Welcome Back
          </v-card-title>
          
          <v-card-text>
            <v-form @submit.prevent="handleLogin" ref="form">
              <v-alert
                v-if="error"
                type="error"
                variant="tonal"
                class="mb-4"
                closable
                @click:close="error = ''"
              >
                {{ error }}
              </v-alert>
              
              <v-text-field
                v-model="email"
                label="Email"
                prepend-inner-icon="mdi-email"
                variant="outlined"
                :rules="[v => !!v || 'Email is required', emailRule]"
                required
              ></v-text-field>
              
              <v-text-field
                v-model="password"
                label="Password"
                prepend-inner-icon="mdi-lock"
                variant="outlined"
                type="password"
                :rules="[v => !!v || 'Password is required']"
                required
              ></v-text-field>
              
              <v-btn
                type="submit"
                color="primary"
                size="large"
                block
                class="mt-4"
                :loading="loading"
              >
                Login
              </v-btn>
            </v-form>
          </v-card-text>
          
          <v-card-actions class="justify-center">
            <v-btn
              variant="text"
              @click="$router.push('/signup')"
            >
              Don't have an account? Sign up
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'LoginView',
  data() {
    return {
      email: '',
      password: '',
      loading: false,
      error: '',
      emailRule: v => /.+@.+\..+/.test(v) || 'Email must be valid'
    }
  },
  methods: {
    ...mapActions(['login']),
    async handleLogin() {
      if (!this.$refs.form.validate()) return
      
      this.loading = true
      this.error = ''
      
      try {
        await this.login({ email: this.email, password: this.password })
        this.$router.push('/dashboard')
      } catch (error) {
        this.error = error.response?.data?.message || 'Login failed. Please check your credentials.'
      } finally {
        this.loading = false
      }
    }
  }
}
</script>
