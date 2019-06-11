<template>
  <div>
    <b-container fluid>
      <b-row class='my-1'>
        <b-col sm='2' lg='1'>
          <label for='OwnerName'>Produtor:</label>
        </b-col>
        <b-col sm='2' lg='1'>
          <b-form-input id='OwnerName' type='text'></b-form-input>
        </b-col>
      </b-row>
      <b-button v-on:click='triggerRequest'>Pesquisar</b-button>
    </b-container>
    <div>
      <div>
        <hr>
        <div class='chart-wrapper'>
          <chart id='chart' :options='plotData'></chart>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'OwnerForm',
  data: () => ({
    chartOptionsBar: {
      xAxis: { data: ['Q1', 'Q2', 'Q3', 'Q4'] },
      yAxis: { type: 'value' },
      series: [{ type: 'bar', data: [63, 75, 24, 92] }]
    },
    chartOptionsLine: {
      xAxis: { data: ['Q1', 'Q2', 'Q3', 'Q4'] },
      yAxis: { type: 'value' },
      series: [{ type: 'line', data: [63, 75, 24, 92] }],
      title: {
        text: 'Quarterly Sales Results',
        x: 'center',
        textStyle: { fontSize: 24 }
      },
      color: ['#127ac2']
    },
    plotData: {
      xAxis: { data: [] },
      yAxis: { type: 'value' },
      series: [{ type: 'line', data: [] }],
      title: {
        text: 'Quarterly Sales Results',
        x: 'center',
        textStyle: { fontSize: 24 }
      },
      color: ['#127ac2', '#f1111', '#f83c46']
    }
  }),
  methods: {
    triggerRequest: function () {
      const OwnerName = document.querySelector('#OwnerName').value
      axios
        .get('http://localhost:5000/byOwner?owner=' + OwnerName)
        .then(response => {
          let dates = response.data.map(info => info.send_data)
          let temperature = response.data.map(info => info.temperature)
          let moisture = response.data.map(info => info.moisture)
          let pressure = response.data.map(info => info.pressure)
          this.plotData.xAxis = { data: dates }
          this.plotData.series = [
            { type: 'line', data: temperature },
            { type: 'line', data: moisture },
            { type: 'line', data: pressure }
          ]
        })
    }
  }
}
</script>
