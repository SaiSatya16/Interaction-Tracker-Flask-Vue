<!-- frontend/src/views/InteractionDetailView.vue -->
<template>
    <v-container v-if="currentInteraction">
      <v-row>
        <v-col cols="12">
          <v-btn @click="$router.go(-1)" text prepend-icon="mdi-arrow-left">Back</v-btn>
          <h1 class="text-h4 font-weight-medium mt-2">Interaction Details</h1>
        </v-col>
      </v-row>
  
      <v-row>
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
        saving: false
      }
    },
    methods: {
      ...mapActions(['updateInteraction']),
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
        } catch (error) {
          console.error('Error updating notes:', error)
        } finally {
          this.saving = false
        }
      },
      async fetchInteractionDetails() {
        try {
          // You'll need to add this method to your store
          const response = await fetch(`http://localhost:5000/api/interactions/${this.$route.params.id}`, {
            headers: {
              'Authorization': `Bearer ${localStorage.getItem('token')}`
            }
          })
          const data = await response.json()
          this.currentInteraction = data
          this.notes = data.notes
        } catch (error) {
          console.error('Error fetching interaction details:', error)
        }
      }
    },
    created() {
      this.fetchInteractionDetails()
    }
  }
  </script>
  