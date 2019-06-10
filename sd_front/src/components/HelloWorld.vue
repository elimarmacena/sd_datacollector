<template>
  <chart :options='chartOptionsBar'></chart>
</template>
<script>
export default {
  name: 'HelloWorld',
  data: () => ({
    chartOptionsBar: {
      xAxis: { data: ['Q1', 'Q2', 'Q3', 'Q4'] },
      yAxis: { type: 'value' },
      series: [{ type: 'bar', data: [63, 75, 24, 92] }]
    }
  })
}
</script>

<style scoped>
</style>
