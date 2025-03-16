<!-- frontend/src/views/NewInteractionView.vue -->
<template>
  <v-container>
    <v-row>
      <v-col cols="12">
        <v-btn @click="$router.go(-1)" text prepend-icon="mdi-arrow-left">Back</v-btn>
        <h1 class="text-h4 font-weight-medium mt-2">Log New Interaction</h1>
      </v-col>
    </v-row>

    <v-row>
      <v-col cols="12" md="8" class="mx-auto">
        <v-card elevation="2" rounded="lg" class="pa-4">
          <v-form @submit.prevent="handleSubmit">
            <v-row>
              <v-col cols="12">
                <v-switch
                  v-model="isNewContact"
                  label="New Contact"
                  color="primary"
                  hide-details
                ></v-switch>
              </v-col>

              <v-col cols="12">
                <v-autocomplete
                  v-if="!isNewContact"
                  v-model="newInteraction.contact_name"
                  :items="contactNames"
                  label="Select Contact"
                  required
                  variant="outlined"
                  autocomplete="off"
                ></v-autocomplete>
                <v-text-field
                  v-else
                  v-model="newInteraction.contact_name"
                  label="New Contact Name"
                  required
                  variant="outlined"
                ></v-text-field>
              </v-col>

              <v-col cols="12">
                <v-select
                  v-model="newInteraction.interaction_type"
                  :items="interactionTypes"
                  label="Interaction Type"
                  required
                  variant="outlined"
                ></v-select>
              </v-col>

              <v-col cols="12">
                <v-textarea
                  v-model="newInteraction.notes"
                  label="Notes"
                  variant="outlined"
                  rows="4"
                ></v-textarea>
              </v-col>

              <v-col cols="12">
                <v-combobox
                  v-model="newInteraction.tags"
                  label="Tags"
                  multiple
                  chips
                  variant="outlined"
                  hint="Press Enter to add a tag"
                  persistent-hint
                ></v-combobox>
              </v-col>

              <v-col cols="12" class="d-flex justify-end">
                <v-btn
                  type="submit"
                  color="primary"
                  size="large"
                  :loading="loading"
                >
                  Save Interaction
                </v-btn>
              </v-col>
            </v-row>
          </v-form>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: 'NewInteractionView',
  data() {
    return {
      isNewContact: false,
      loading: false,
      newInteraction: {
        contact_name: '',
        interaction_type: '',
        notes: '',
        tags: []
      },
      interactionTypes: ['Meeting', 'Call', 'Email', 'Social', 'Other']
    }
  },
  computed: {
    ...mapState(['contacts']),
    contactNames() {
      return this.contacts.map(contact => contact.name)
    }
  },
  methods: {
    ...mapActions(['fetchContacts', 'addInteraction', 'addContact']),
    async handleSubmit() {
      this.loading = true
      try {
        // If new contact, create it first
        if (this.isNewContact) {
          await this.addContact({
            name: this.newInteraction.contact_name,
            notes: [],
            tags: []
          })
        }
        
        // Add the interaction
        await this.addInteraction(this.newInteraction)
        this.$router.push('/dashboard')
      } catch (error) {
        console.error('Error saving interaction:', error)
      } finally {
        this.loading = false
      }
    }
  },
  created() {
    this.fetchContacts()
  }
}
</script>
