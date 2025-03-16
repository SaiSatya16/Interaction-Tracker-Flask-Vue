<template>
  <v-container>
    <v-row>
      <v-col cols="12" class="d-flex justify-space-between align-center">
        <h1 class="text-h4 font-weight-medium">Your Interactions</h1>
        <v-btn 
          color="primary" 
          @click="$router.push('/interactions/new')" 
          prepend-icon="mdi-plus"
          elevation="2"
          rounded
        >
          Log Interaction
        </v-btn>
      </v-col>
    </v-row>

    <v-row>
      <v-col cols="12">
        <v-card elevation="2" rounded="lg">
          <v-data-table
            :headers="headers"
            :items="interactions"
            :items-per-page="10"
            class="elevation-0"
            @click:row="viewInteractionDetails"
          >
            <!-- <template v-slot:item.timestamp="{ item }"> -->
              <template #[slotName]="{ item }">

              {{ formatDate(item.timestamp) }}
            </template>
            <!-- <template v-slot:item.tags="{ item }"> -->
            <template #[slotName2]="{ item }">
              <v-chip
                v-for="tag in item.tags"
                :key="tag"
                size="small"
                class="mr-1"
                color="secondary"
                variant="outlined"
              >
                {{ tag }}
              </v-chip>
            </template>
          </v-data-table>
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
  data() {
    return {
      headers: [
        { title: 'Contact', key: 'contact_name' },
        { title: 'Type', key: 'interaction_type' },
        { title: 'Date', key: 'timestamp' },
        { title: 'Tags', key: 'tags' }
      ]
    }
  },
  computed: {
    ...mapState(['interactions']),
    slotName() {
      return 'item.timestamp'
    },
    slotName2() {
      return 'item.tags'
    }
  },
  methods: {
    ...mapActions(['fetchInteractions']),
    formatDate(date) {
      return moment(date).format('MMMM D, YYYY')
    },
    viewInteractionDetails(item) {
      this.$router.push(`/interactions/${item._id}`)
    }
  },
  created() {
    this.fetchInteractions()
  }
}
</script>
