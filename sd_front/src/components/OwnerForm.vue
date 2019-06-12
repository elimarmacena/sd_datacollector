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
      <hr>
      <div>
        <chart id='chart' :options='temperaturePlot'></chart>
        <chart id='chart' :options='moisturePlot'></chart>
        <chart id='chart' :options='pressurePlot'></chart>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'OwnerForm',
  data: () => ({
    temperaturePlot: {
      xAxis: { data: [] },
      yAxis: { type: 'value' },
      series: [{ type: 'line', data: [] }],
      title: {
        left: 'center',
        show: true,
        text: 'Resultados Temperatura',
        textStyle: { fontSize: 24 },
        color: '#000000'
      },
      color: ['#d88227']
    },
    moisturePlot: {
      xAxis: { data: [] },
      yAxis: { type: 'value' },
      series: [{ type: 'line', data: [] }],
      title: {
        left: 'center',
        show: true,
        text: 'Resultados Umidade',
        textStyle: { fontSize: 24 }
      },
      color: ['#2f9bd6']
    },
    pressurePlot: {
      xAxis: { data: [] },
      yAxis: { type: 'value' },
      series: [{ type: 'line', data: [] }],
      title: {
        left: 'center',
        show: true,
        text: 'Resultados Pressao',
        textStyle: { fontSize: 24 }
      },
      color: ['#d3f20e']
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
          this.temperaturePlot.xAxis = {data: dates}
          this.temperaturePlot.series = [
            {type: 'line', data: temperature}
          ]
          this.moisturePlot.xAxis = {data: dates}
          this.moisturePlot.series = [
            {type: 'line', data: moisture}
          ]
          this.pressurePlot.xAxis = {data: dates}
          this.pressurePlot.series = [
            {type: 'line', data: pressure}
          ]
        })
    }
  }
}
</script>
