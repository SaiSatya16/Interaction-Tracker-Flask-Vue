<template>
    <v-container>
      <h1>Interactions</h1>
      <v-btn color="primary" @click="dialog = true">Log New Interaction</v-btn>
  
      <v-dialog v-model="dialog" max-width="500px">
        <v-card>
          <v-card-title>New Interaction</v-card-title>
          <v-card-text>
            <v-form @submit.prevent="handleSubmit">
              <v-select v-model="newInteraction.contact_name" :items="contactNames" label="Contact"></v-select>
              <v-select v-model="newInteraction.interaction_type" :items="interactionTypes" label="Type"></v-select>
              <v-textarea v-model="newInteraction.notes" label="Notes"></v-textarea>
              <v-combobox v-model="newInteraction.tags" label="Tags" multiple chips></v-combobox>
              <v-btn type="submit" color="primary">Save</v-btn>
            </v-form>
          </v-card-text>
        </v-card>
      </v-dialog>
  
      <v-data-table :headers="headers" :items="interactions" class="mt-5">
        <template #[slotName]="{ item }">

          {{ formatDate(item.timestamp) }}
        </template>
        <template #[slotName2]="{ item }">

          <v-icon small class="mr-2" @click="editInteraction(item)">mdi-pencil</v-icon>
          <v-icon small @click="deleteInteraction(item._id)">mdi-delete</v-icon>
        </template>
      </v-data-table>
    </v-container>
  </template>
  
  <script>
  import { mapState, mapActions } from 'vuex'
  import moment from 'moment'
  
  export default {
    name: 'InteractionsView',
    data() {
      return {
        dialog: false,
        newInteraction: {
          contact_name: '',
          interaction_type: '',
          notes: '',
          tags: []
        },
        headers: [
          { text: 'Contact', value: 'contact_name' },
          { text: 'Type', value: 'interaction_type' },
          { text: 'Date', value: 'timestamp' },
          { text: 'Actions', value: 'actions', sortable: false }
        ],
        interactionTypes: ['Meeting', 'Call', 'Email', 'Social', 'Other']
      }
    },
    computed: {
      ...mapState(['interactions', 'contacts']),
      contactNames() {
        return this.contacts.map(contact => contact.name)
      },
      slotName() {
        return 'item.actions'
      },
      slotName2() {
        return 'item.actions'
      }
    },
    methods: {
      ...mapActions(['fetchInteractions', 'fetchContacts', 'addInteraction', 'updateInteraction', 'deleteInteraction']),
      formatDate(date) {
        return moment(date).format('MMMM D, YYYY')
      },
      async handleSubmit() {
        await this.addInteraction(this.newInteraction)
        this.dialog = false
        this.newInteraction = { contact_name: '', interaction_type: '', notes: '', tags: [] }
      },
      editInteraction(item) {

        // Implement edit functionality
        item.timestamp = new Date(item.timestamp)


      }
    },
    created() {
      this.fetchInteractions()
      this.fetchContacts()
    }
  }
  </script>
  