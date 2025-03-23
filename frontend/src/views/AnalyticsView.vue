<template>
  <v-container>
    <v-card class="mb-6">
      <v-card-title class="headline">
        <v-icon large left>mdi-chart-bar</v-icon>
        Analytics
      </v-card-title>
      
      <v-card flat>
        <v-card-text style="height: 600px;">
          <div class="heatmap-container">
            <v-skeleton-loader
              v-if="loadingHeatmap"
              type="card"
              height="500"
            ></v-skeleton-loader>
            <div v-else-if="!Object.keys(heatmapData).length" class="text-center pa-5">
              <v-icon size="large" color="grey">mdi-chart-timeline-variant</v-icon>
              <p class="text-body-1 mt-2">No interaction data available. Start logging interactions to see your activity.</p>
            </div>
            <heatmap-chart v-else :data="heatmapData"></heatmap-chart>
          </div>
        </v-card-text>
      </v-card>
    </v-card>
  </v-container>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import HeatmapChart from '@/components/HeatmapChart.vue'

export default {
  name: 'AnalyticsView',
  components: {
    HeatmapChart
  },
  data() {
    return {
      loadingHeatmap: true
    }
  },
  computed: {
    ...mapState(['heatmapData'])
  },
  methods: {
    ...mapActions(['fetchHeatmapData']),
    async loadHeatmapData() {
      this.loadingHeatmap = true
      try {
        await this.fetchHeatmapData()
      } catch (error) {
        console.error('Error loading heatmap data:', error)
      } finally {
        this.loadingHeatmap = false
      }
    }
  },
  mounted() {
    this.loadHeatmapData();
  }
}
</script>

<style scoped>
.heatmap-container {
  height: 500px;
  margin-top: 20px;
}
</style>
