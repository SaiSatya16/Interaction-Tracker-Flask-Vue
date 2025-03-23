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
            hover
            item-value="_id"
          >
            <template #[`item.timestamp`]="{ item }">
              {{ formatDate(item.timestamp) }}
            </template>
            <template #[`item.tags`]="{ item }">
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
            <template #item="{ item, props }">
              <tr 
                @click="viewInteractionDetails(item._id)" 
                v-bind="props" 
                style="cursor: pointer;"
              >
                <td>{{ item.contact_name }}</td>
                <td>{{ item.interaction_type }}</td>
                <td>{{ formatDate(item.timestamp) }}</td>
                <td>
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
                </td>
              </tr>
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
    ...mapState(['interactions'])
  },
  methods: {
    ...mapActions(['fetchInteractions']),
    formatDate(date) {
      return moment(date).format('MMM D, YYYY')
    },
    viewInteractionDetails(id) {
      console.log('Interaction clicked:', id);
      if (id) {
        this.$router.push(`/interactions/${id}`);
      } else {
        console.error('Interaction ID is undefined');
      }
    }
  },
  created() {
    this.fetchInteractions()
  }
}
</script>

<style scoped>
.v-data-table tr {
  cursor: pointer;
}
</style>
