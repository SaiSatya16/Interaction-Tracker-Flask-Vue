<template>
    <div class="heatmap-chart">
      <canvas ref="heatmapCanvas"></canvas>
    </div>
  </template>
  
  <script>
  import { Chart, registerables } from 'chart.js'
  import moment from 'moment'
  
  Chart.register(...registerables)
  
  export default {
    name: 'HeatmapChart',
    props: {
      data: {
        type: Object,
        required: true
      }
    },
    data() {
      return {
        chart: null
      }
    },
    watch: {
      data: {
        handler() {
          this.renderChart()
        },
        deep: true
      }
    },
    methods: {
      renderChart() {
        if (this.chart) {
          this.chart.destroy()
        }
  
        const ctx = this.$refs.heatmapCanvas.getContext('2d')
        
        // Prepare data for the chart
        const dates = Object.keys(this.data)
        const counts = Object.values(this.data)
        
        // Create chart
        this.chart = new Chart(ctx, {
          type: 'bar',
          data: {
            labels: dates.map(date => moment(date).format('MMM D')),
            datasets: [{
              label: 'Interactions',
              data: counts,
              backgroundColor: 'rgba(75, 192, 192, 0.6)',
              borderColor: 'rgba(75, 192, 192, 1)',
              borderWidth: 1
            }]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
              y: {
                beginAtZero: true,
                title: {
                  display: true,
                  text: 'Number of Interactions'
                }
              },
              x: {
                title: {
                  display: true,
                  text: 'Date'
                }
              }
            }
          }
        })
      }
    },
    mounted() {
      this.renderChart()
    }
  }
  </script>
  