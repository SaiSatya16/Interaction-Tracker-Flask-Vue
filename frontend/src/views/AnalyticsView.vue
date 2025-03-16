<template>
    <v-container>
      <h1>Analytics</h1>
      
      <v-tabs v-model="tab">
        <v-tab>Interaction Heatmap</v-tab>
        <v-tab>Network Graph</v-tab>
      </v-tabs>
      
      <v-tabs-items v-model="tab">
        <v-tab-item>
          <v-card flat>
            <v-card-title>Interaction Frequency</v-card-title>
            <v-card-text>
              <div class="heatmap-container">
                <heatmap-chart :data="heatmapData"></heatmap-chart>
              </div>
            </v-card-text>
          </v-card>
        </v-tab-item>
        
        <v-tab-item>
          <v-card flat>
            <v-card-title>Relationship Network</v-card-title>
            <v-card-text>
              <div class="network-container">
                <network-graph :data="networkData"></network-graph>
              </div>
            </v-card-text>
          </v-card>
        </v-tab-item>
      </v-tabs-items>
    </v-container>
  </template>
  
  <script>
  import { mapState, mapActions } from 'vuex'
  import HeatmapChart from '@/components/HeatmapChart.vue'
  import NetworkGraph from '@/components/NetworkGraph.vue'
  
  export default {
    name: 'AnalyticsView',
    components: {
      HeatmapChart,
      NetworkGraph
    },
    data() {
      return {
        tab: null
      }
    },
    computed: {
      ...mapState(['heatmapData', 'networkData'])
    },
    methods: {
      ...mapActions(['fetchHeatmapData', 'fetchNetworkData'])
    },
    created() {
      this.fetchHeatmapData()
      this.fetchNetworkData()
    }
  }
  </script>
  
  <style scoped>
  .heatmap-container, .network-container {
    height: 500px;
    width: 100%;
  }
  </style>
  