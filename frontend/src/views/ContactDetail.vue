<template>
    <v-container v-if="currentContact">
      <v-row>
        <v-col cols="12">
          <v-btn @click="$router.go(-1)" text><v-icon>mdi-arrow-left</v-icon> Back</v-btn>
          <h1>{{ currentContact.name }}</h1>
          <v-chip v-for="tag in currentContact.tags" :key="tag" class="ma-1">{{ tag }}</v-chip>
        </v-col>
      </v-row>
  
      <v-row>
        <v-col cols="12" md="6">
          <v-card>
            <v-card-title>Notes</v-card-title>
            <v-card-text>
              <v-list>
                <v-list-item v-for="(note, index) in currentContact.notes" :key="index">
                  <v-list-item-content>
                    <v-list-item-subtitle>{{ formatDate(note.timestamp) }}</v-list-item-subtitle>
                    <v-list-item-title>{{ note.content }}</v-list-item-title>
                  </v-list-item-content>
                </v-list-item>
              </v-list>
              <v-form @submit.prevent="addNote">
                <v-textarea v-model="newNote" label="Add a note"></v-textarea>
                <v-btn type="submit" color="primary">Add Note</v-btn>
              </v-form>
            </v-card-text>
          </v-card>
        </v-col>
  
        <v-col cols="12" md="6">
          <v-card>
            <v-card-title>Recent Interactions</v-card-title>
            <v-card-text>
              <v-list>
                <v-list-item v-for="interaction in currentContact.interactions" :key="interaction._id">
                  <v-list-item-content>
                    <v-list-item-title>{{ interaction.interaction_type }}</v-list-item-title>
                    <v-list-item-subtitle>{{ formatDate(interaction.timestamp) }}</v-list-item-subtitle>
                    <p>{{ interaction.notes }}</p>
                  </v-list-item-content>
                </v-list-item>
              </v-list>
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
    name: 'ContactDetail',
    data() {
      return {
        newNote: ''
      }
    },
    computed: {
      ...mapState(['currentContact'])
    },
    methods: {
      ...mapActions(['fetchContact', 'addNoteToContact']),
      formatDate(date) {
        return moment(date).format('MMMM D, YYYY')
      },
      async addNote() {
        if (this.newNote.trim()) {
          await this.addNoteToContact({ id: this.$route.params.id, note: this.newNote })
          this.newNote = ''
        }
      }
    },
    created() {
      this.fetchContact(this.$route.params.id)
    }
  }
  </script>
  