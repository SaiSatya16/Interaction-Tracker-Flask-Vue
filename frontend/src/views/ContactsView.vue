<template>
    <v-container>
      <h1>Contacts</h1>
      <v-btn color="primary" @click="dialog = true">Add New Contact</v-btn>
  
      <v-dialog v-model="dialog" max-width="500px">
        <v-card>
          <v-card-title>New Contact</v-card-title>
          <v-card-text>
            <v-form @submit.prevent="handleSubmit">
              <v-text-field v-model="newContact.name" label="Name"></v-text-field>
              <v-textarea v-model="newContact.notes" label="Notes"></v-textarea>
              <v-combobox v-model="newContact.tags" label="Tags" multiple chips></v-combobox>
              <v-btn type="submit" color="primary">Save</v-btn>
            </v-form>
          </v-card-text>
        </v-card>
      </v-dialog>
  
      <v-data-table :headers="headers" :items="contacts" class="mt-5">
        <template #[slotName]="{ item }">
          <v-icon small class="mr-2" @click="viewContact(item._id)">mdi-eye</v-icon>
        <v-icon small class="mr-2" @click="editContact(item)">mdi-pencil</v-icon>
        <v-icon small @click="confirmDelete(item._id)">mdi-delete</v-icon>
      </template>
    </v-data-table>

    <v-dialog v-model="deleteDialog" max-width="300px">
      <v-card>
        <v-card-title>Confirm Delete</v-card-title>
        <v-card-text>Are you sure you want to delete this contact?</v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="error" @click="handleDelete">Delete</v-btn>
          <v-btn @click="deleteDialog = false">Cancel</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: 'ContactsView',
  data() {
    return {
      dialog: false,
      deleteDialog: false,
      deleteId: null,
      newContact: {
        name: '',
        notes: [],
        tags: []
      },
      headers: [
        { text: 'Name', value: 'name' },
        { text: 'Tags', value: 'tags' },
        { text: 'Actions', value: 'actions', sortable: false }
      ]
    }
  },
  computed: {
    ...mapState(['contacts']),
    slotName() {
      return 'item.actions'
    }
  },
  methods: {
    ...mapActions(['fetchContacts', 'addContact', 'updateContact', 'deleteContact']),
    async handleSubmit() {
      await this.addContact(this.newContact)
      this.dialog = false
      this.newContact = { name: '', notes: [], tags: [] }
    },
    viewContact(id) {
      this.$router.push(`/contacts/${id}`)
    },
    editContact(item) {
      // Implement edit functionality
      this.newContact = { ...item }
      this.dialog = true
    },
    confirmDelete(id) {
      this.deleteId = id
      this.deleteDialog = true
    },
    async handleDelete() {
      await this.deleteContact(this.deleteId)
      this.deleteDialog = false
      this.deleteId = null
    }
  },
  created() {
    this.fetchContacts()
  }
}
</script>
  