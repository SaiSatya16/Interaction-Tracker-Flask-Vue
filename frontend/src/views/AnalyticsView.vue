<template>
  <v-container>
    <v-card class="mb-6">
      <v-card-title class="headline">
        <v-icon large left>mdi-chart-bar</v-icon>
        Analytics
      </v-card-title>
      
      <v-tabs v-model="tab" background-color="primary" dark grow>
        <v-tab>
          <v-icon left>mdi-calendar-month</v-icon>
          Interaction Heatmap
        </v-tab>
        <v-tab>
          <v-icon left>mdi-account-network</v-icon>
          Network Graph
        </v-tab>
      </v-tabs>
      
      <v-tabs-items v-model="tab">
        <v-tab-item>
          <v-card flat>
            <v-card-text>
              <div class="heatmap-container">
                <v-skeleton-loader
                  v-if="!Object.keys(heatmapData).length"
                  type="card"
                  height="500"
                ></v-skeleton-loader>
                <heatmap-chart v-else :data="heatmapData"></heatmap-chart>
              </div>
            </v-card-text>
          </v-card>
        </v-tab-item>
        
        <v-tab-item>
          <v-card flat>
            <v-card-text>
              <div class="network-container">
                <v-skeleton-loader
                  v-if="!networkData.nodes || !networkData.nodes.length"
                  type="card"
                  height="500"
                ></v-skeleton-loader>
                <network-graph v-else :data="networkData"></network-graph>
              </div>
            </v-card-text>
          </v-card>
        </v-tab-item>
      </v-tabs-items>
    </v-card>
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
      tab: 0
    }
  },
  computed: {
    ...mapState(['heatmapData', 'networkData'])
  },
  methods: {
    ...mapActions(['fetchHeatmapData', 'fetchNetworkData'])
  },
  mounted() {
    this.$nextTick(() => {
      this.fetchHeatmapData()
      this.fetchNetworkData()
    })
  }
}
</script>

<style scoped>
.network-container {
  height: 600px;
  margin-top: 20px;
}

.heatmap-container {
  height: 500px;
  margin-top: 20px;
}
</style>

