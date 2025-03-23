<template>
  <v-container>
    <v-row>
      <v-col cols="12">
        <v-btn @click="$router.go(-1)" text prepend-icon="mdi-arrow-left">Back</v-btn>
        <h1 class="text-h4 font-weight-medium mt-2">Interaction Details</h1>
      </v-col>
    </v-row>

    <v-row v-if="loading">
      <v-col cols="12" md="8" class="mx-auto">
        <v-skeleton-loader type="card" height="400"></v-skeleton-loader>
      </v-col>
    </v-row>

    <v-row v-else-if="currentInteraction">
      <v-col cols="12" md="8" class="mx-auto">
        <v-card elevation="2" rounded="lg" class="pa-4">
          <v-card-text>
            <v-row>
              <v-col cols="12" md="6">
                <p class="text-subtitle-1 font-weight-bold">Contact</p>
                <p class="text-body-1">{{ currentInteraction.contact_name }}</p>
              </v-col>
              
              <v-col cols="12" md="6">
                <p class="text-subtitle-1 font-weight-bold">Type</p>
                <p class="text-body-1">{{ currentInteraction.interaction_type }}</p>
              </v-col>
              
              <v-col cols="12" md="6">
                <p class="text-subtitle-1 font-weight-bold">Date</p>
                <p class="text-body-1">{{ formatDate(currentInteraction.timestamp) }}</p>
              </v-col>
              
              <v-col cols="12" md="6">
                <p class="text-subtitle-1 font-weight-bold">Tags</p>
                <div>
                  <v-chip
                    v-for="tag in currentInteraction.tags"
                    :key="tag"
                    class="mr-1 mb-1"
                    color="secondary"
                    variant="outlined"
                  >
                    {{ tag }}
                  </v-chip>
                </div>
              </v-col>
              
              <v-col cols="12">
                <p class="text-subtitle-1 font-weight-bold">Notes</p>
                <v-textarea
                  v-model="notes"
                  variant="outlined"
                  rows="6"
                  :readonly="!editing"
                  :hide-details="!editing"
                ></v-textarea>
              </v-col>
            </v-row>
          </v-card-text>
          
          <v-card-actions class="justify-end">
            <v-btn
              v-if="!editing"
              color="primary"
              @click="startEditing"
              prepend-icon="mdi-pencil"
            >
              Edit Notes
            </v-btn>
            <template v-else>
              <v-btn
                color="error"
                variant="text"
                @click="cancelEditing"
              >
                Cancel
              </v-btn>
              <v-btn
                color="success"
                @click="saveNotes"
                :loading="saving"
              >
                Save Changes
              </v-btn>
            </template>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>

    <v-row v-else>
      <v-col cols="12" class="text-center">
        <p class="text-h6">Interaction not found</p>
        <v-btn color="primary" @click="$router.push('/dashboard')" class="mt-4">
          Return to Dashboard
        </v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { mapActions } from 'vuex'
import moment from 'moment'

export default {
  name: 'InteractionDetailView',
  data() {
    return {
      currentInteraction: null,
      notes: '',
      editing: false,
      saving: false,
      loading: true,
      error: null
    }
  },
  methods: {
    ...mapActions(['fetchInteractionById', 'updateInteraction']),
    
    formatDate(date) {
      return moment(date).format('MMMM D, YYYY, h:mm a')
    },
    
    startEditing() {
      this.editing = true
    },
    
    cancelEditing() {
      this.notes = this.currentInteraction.notes
      this.editing = false
    },
    
    async saveNotes() {
      this.saving = true
      try {
        await this.updateInteraction({
          id: this.currentInteraction._id,
          data: { notes: this.notes }
        })
        this.currentInteraction.notes = this.notes
        this.editing = false
        // Show success notification if you have a notification system
      } catch (error) {
        console.error('Error updating notes:', error)
        // Show error notification
      } finally {
        this.saving = false
      }
    },
    
    async fetchInteractionDetails() {
      this.loading = true
      try {
        this.currentInteraction = await this.fetchInteractionById(this.$route.params.id)
        this.notes = this.currentInteraction.notes
      } catch (error) {
        this.error = error.message || 'Failed to load interaction details'
      } finally {
        this.loading = false
      }
    }
  },
  created() {
    this.fetchInteractionDetails()
  }
}
</script>
