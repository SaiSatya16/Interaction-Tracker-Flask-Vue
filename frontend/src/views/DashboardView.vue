<template>
    <v-container>
      <h1>Dashboard</h1>
      <v-row>
        <v-col cols="12" md="6">
          <v-card>
            <v-card-title>Recent Interactions</v-card-title>
            <v-card-text>
              <v-list>
                <v-list-item v-for="interaction in recentInteractions" :key="interaction._id">
                  <v-list-item-content>
                    <v-list-item-title>{{ interaction.contact_name }}</v-list-item-title>
                    <v-list-item-subtitle>{{ interaction.interaction_type }} - {{ formatDate(interaction.timestamp) }}</v-list-item-subtitle>
                  </v-list-item-content>
                </v-list-item>
              </v-list>
            </v-card-text>
          </v-card>
        </v-col>
        <v-col cols="12" md="6">
          <v-card>
            <v-card-title>Quick Actions</v-card-title>
            <v-card-text>
              <v-btn to="/interactions" color="primary" class="mr-2">Log Interaction</v-btn>
              <v-btn to="/contacts" color="secondary">Manage Contacts</v-btn>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </template>
  
  <script>
  import { mapState, mapActions } from 'vuex'
  import moment from 'moment'
  
  export default {
    name: 'DashboardView',
    computed: {
      ...mapState(['interactions']),
      recentInteractions() {
        return this.interactions.slice(0, 5)
      }
    },
    methods: {
      ...mapActions(['fetchInteractions']),
      formatDate(date) {
        return moment(date).format('MMMM D, YYYY')
      }
    },
    created() {
      this.fetchInteractions()
    }
  }
  </script>
  