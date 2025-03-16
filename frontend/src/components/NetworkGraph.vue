<template>
    <div class="network-graph" ref="networkGraph"></div>
  </template>
  
  <script>
  import * as d3 from 'd3'
  
  export default {
    name: 'NetworkGraph',
    props: {
      data: {
        type: Object,
        required: true
      }
    },
    watch: {
      data: {
        handler() {
          this.renderGraph()
        },
        deep: true
      }
    },
    methods: {
      renderGraph() {
        // Clear previous graph
        d3.select(this.$refs.networkGraph).selectAll('*').remove()
        
        if (!this.data.nodes || !this.data.links || this.data.nodes.length === 0) {
          return
        }
        
        const width = this.$refs.networkGraph.clientWidth
        const height = this.$refs.networkGraph.clientHeight
        
        const svg = d3.select(this.$refs.networkGraph)
          .append('svg')
          .attr('width', width)
          .attr('height', height)
        
        // Create a force simulation
        const simulation = d3.forceSimulation(this.data.nodes)
          .force('link', d3.forceLink(this.data.links).id(d => d.id).distance(100))
          .force('charge', d3.forceManyBody().strength(-300))
          .force('center', d3.forceCenter(width / 2, height / 2))
        
        // Draw links
        const link = svg.append('g')
          .selectAll('line')
          .data(this.data.links)
          .enter()
          .append('line')
          .attr('stroke-width', d => Math.sqrt(d.value))
          .attr('stroke', '#999')
        
        // Draw nodes
        const node = svg.append('g')
          .selectAll('circle')
          .data(this.data.nodes)
          .enter()
          .append('circle')
          .attr('r', d => d.type === 'user' ? 15 : 10)
          .attr('fill', d => d.type === 'user' ? '#ff7f0e' : '#1f77b4')
          .call(this.drag(simulation))
        
        // Add labels
        const label = svg.append('g')
          .selectAll('text')
          .data(this.data.nodes)
          .enter()
          .append('text')
          .text(d => d.name)
          .attr('font-size', 12)
          .attr('dx', 15)
          .attr('dy', 4)
        
        // Update positions on simulation tick
        simulation.on('tick', () => {
          link
            .attr('x1', d => d.source.x)
            .attr('y1', d => d.source.y)
            .attr('x2', d => d.target.x)
            .attr('y2', d => d.target.y)
          
          node
            .attr('cx', d => d.x)
            .attr('cy', d => d.y)
          
          label
            .attr('x', d => d.x)
            .attr('y', d => d.y)
        })
      },
      drag(simulation) {
        function dragstarted(event) {
          if (!event.active) simulation.alphaTarget(0.3).restart()
          event.subject.fx = event.subject.x
          event.subject.fy = event.subject.y
        }
        
        function dragged(event) {
          event.subject.fx = event.x
          event.subject.fy = event.y
        }
        
        function dragended(event) {
          if (!event.active) simulation.alphaTarget(0)
          event.subject.fx = null
          event.subject.fy = null
        }
        
        return d3.drag()
          .on('start', dragstarted)
          .on('drag', dragged)
          .on('end', dragended)
      }
    },
    mounted() {
      this.renderGraph()
    }
  }
  </script>
  