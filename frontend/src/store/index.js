import { createStore } from 'vuex'
import axios from 'axios'

const API_URL = 'http://localhost:5000/api'

export default createStore({
  state: {
    token: localStorage.getItem('token') || '',
    user: null,
    interactions: [],
    contacts: [],
    currentContact: null,
    heatmapData: {},
    networkData: {}
  },
  mutations: {
    setToken(state, token) {
      state.token = token
    },
    setInteractions(state, interactions) {
      state.interactions = interactions
    },
    addInteraction(state, interaction) {
      state.interactions.unshift(interaction)
    },
    updateInteraction(state, updatedInteraction) {
      const index = state.interactions.findIndex(i => i._id === updatedInteraction._id)
      if (index !== -1) {
        state.interactions.splice(index, 1, updatedInteraction)
      }
    },
    removeInteraction(state, id) {
      state.interactions = state.interactions.filter(i => i._id !== id)
    },
    setContacts(state, contacts) {
      state.contacts = contacts
    },
    setCurrentContact(state, contact) {
      state.currentContact = contact
    },
    addContact(state, contact) {
      state.contacts.push(contact) 
    },
    updateContact(state, updatedContact) {
        const index = state.contacts.findIndex(c => c._id === updatedContact._id)
        if (index !== -1) {
          state.contacts.splice(index, 1, updatedContact)
        }
      },
      removeContact(state, id) {
        state.contacts = state.contacts.filter(c => c._id !== id)
      },
      setHeatmapData(state, data) {
        state.heatmapData = data
      },
      setNetworkData(state, data) {
        state.networkData = data
      },
      setDarkMode(state, isDark) {
        state.darkMode = isDark
      },
      // In mutations:
setCurrentInteraction(state, interaction) {
  state.currentInteraction = interaction
}

    },
    actions: {
      async login({ commit }, credentials) {
        const response = await axios.post(`${API_URL}/auth/login`, credentials)
        const token = response.data.token
        localStorage.setItem('token', token)
        commit('setToken', token)
        axios.defaults.headers.common['Authorization'] = `Bearer ${token}`
      },
      async signup(_, userData) {
        await axios.post(`${API_URL}/auth/signup`, userData)
      },
      async logout({ commit }) {
        localStorage.removeItem('token')
        commit('setToken', '')
        delete axios.defaults.headers.common['Authorization']
      },
      async fetchInteractions({ commit }) {
        const response = await axios.get(`${API_URL}/interactions`)
        commit('setInteractions', response.data)
      },
      async addInteraction({ commit }, interactionData) {
        const response = await axios.post(`${API_URL}/interactions`, interactionData)
        commit('addInteraction', response.data)
      },
      async updateInteraction({ commit }, { id, data }) {
        const response = await axios.put(`${API_URL}/interactions/${id}`, data)
        commit('updateInteraction', response.data)
      },
      async deleteInteraction({ commit }, id) {
        await axios.delete(`${API_URL}/interactions/${id}`)
        commit('removeInteraction', id)
      },
      async fetchContacts({ commit }) {
        const response = await axios.get(`${API_URL}/contacts`)
        commit('setContacts', response.data)
      },
      async fetchContact({ commit }, id) {
        const response = await axios.get(`${API_URL}/contacts/${id}`)
        commit('setCurrentContact', response.data)
      },
      async addContact({ commit }, contactData) {
        const response = await axios.post(`${API_URL}/contacts`, contactData)
        commit('addContact', response.data)
      },
      async updateContact({ commit }, { id, data }) {
        const response = await axios.put(`${API_URL}/contacts/${id}`, data)
        commit('updateContact', response.data)
      },
      async deleteContact({ commit }, id) {
        await axios.delete(`${API_URL}/contacts/${id}`)
        commit('removeContact', id)
      },
      async addNoteToContact({ commit }, { id, note }) {
        const response = await axios.post(`${API_URL}/contacts/${id}/notes`, { content: note })
        commit('setCurrentContact', response.data)
      },
// In frontend/src/store/index.js - update these actions
async fetchHeatmapData({ commit }) {
  try {
    const response = await axios.get(`${API_URL}/analytics/heatmap`)
    commit('setHeatmapData', response.data)
    return response.data
  } catch (error) {
    console.error('Error fetching heatmap data:', error)
    throw error
  }
},

async fetchNetworkData({ commit }) {
  try {
    const response = await axios.get(`${API_URL}/analytics/network`);
    // Make sure we're not modifying the response directly
    const processedData = { ...response.data };
    commit('setNetworkData', processedData);
    return processedData;
  } catch (error) {
    console.error('Error fetching network data:', error);
    throw error;
  }
}
,
      // In src/store/index.js, add or modify these actions:

async fetchInteractionById({ commit }, id) {
  try {
    const response = await axios.get(`${API_URL}/interactions/${id}`)
    commit('setCurrentInteraction', response.data)
    return response.data
  } catch (error) {
    console.error('Error fetching interaction:', error)
    throw error
  }
},

async updateInteractionNotes({ commit }, { id, notes }) {
  try {
    const response = await axios.put(`${API_URL}/interactions/${id}`, { notes })
    commit('updateInteraction', response.data)
    return response.data
  } catch (error) {
    console.error('Error updating interaction notes:', error)
    throw error
  }
}
,
      
      async toggleDarkMode({ commit }, isDark) {
        commit('setDarkMode', isDark)
        localStorage.setItem('theme', isDark ? 'dark' : 'light')
      },
    },
    getters: {
      isAuthenticated: state => !!state.token
    }
  })
  
