<template>
  <div>
    <b-container fluid>
      <b-row class='my-1'>
        <b-col sm='2' lg='1'>
          <label for='dateMin'>Data Inicio:</label>
        </b-col>
        <b-col sm='2' lg='2'>
          <b-form-input id='dateMin' type='date'></b-form-input>
        </b-col>
      </b-row>
      <b-row class='my-1'>
        <b-col sm='2' lg='1'>
          <label for='dateMax'>Data Limite:</label>
        </b-col>
        <b-col sm='2' lg='2'>
          <b-form-input id='dateMax' type='date'></b-form-input>
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
      tooltip: {
        trigger: 'axis'
      },
      toolbox: {
        show: true,
        feature: {
          dataZoom: {
            yAxisIndex: 'none'
          },
          restore: {},
          saveAsImage: {}
        }
      },
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
      tooltip: {
        trigger: 'axis'
      },
      toolbox: {
        show: true,
        feature: {
          dataZoom: {
            yAxisIndex: 'none'
          },
          restore: {},
          saveAsImage: {}
        }
      },
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
      tooltip: {
        trigger: 'axis'
      },
      toolbox: {
        show: true,
        feature: {
          dataZoom: {
            yAxisIndex: 'none'
          },
          restore: {},
          saveAsImage: {}
        }
      },
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
      const dateMin = document.querySelector('#dateMin').value
      const dateMax = document.querySelector('#dateMax').value
      const colors = ['#177B9A', '#F29918', '#B4CED9', '#A2C75D', '#52C1DC']
      axios
        .get('http://localhost:5000/interValDate?dateMin=' + dateMin + '&dateMax=' + dateMax)
        .then(response => {
          let owners = response.data.map(info => info.owner)
          let unicOwners = owners.filter((value, index, a) => a.indexOf(value) === index)
          let dates = response.data.map(info => info.send_data)
          this.temperaturePlot.xAxis = {data: dates}
          this.moisturePlot.xAxis = {data: dates}
          this.pressurePlot.xAxis = {data: dates}
          var seriesTemperature = []
          var seriesMoisture = []
          var seriesPressure = []
          for (let i = 0; i < unicOwners.length; i++) {
            let ownerTemperature = response.data.filter(obj => obj.owner === unicOwners[i]).map(obj => obj.temperature)
            let ownerMoisture = response.data.filter(obj => obj.owner === unicOwners[i]).map(obj => obj.moisture)
            let ownerPressure = response.data.filter(obj => obj.owner === unicOwners[i]).map(obj => obj.pressure)
            let colorInfo = {color: colors[i]}
            let tempStruct = {type: 'line', data: ownerTemperature, name: unicOwners[i], lineStyle: colorInfo}
            let moistStruct = {type: 'line', data: ownerMoisture, name: unicOwners[i], lineStyle: colorInfo}
            let pressStruc = {type: 'line', data: ownerPressure, name: unicOwners[i], lineStyle: colorInfo}
            seriesTemperature.push(tempStruct)
            seriesMoisture.push(moistStruct)
            seriesPressure.push(pressStruc)
          }
          this.temperaturePlot.series = seriesTemperature
          this.moisturePlot.series = seriesMoisture
          this.pressurePlot.series = seriesPressure
        })
    }
  }
}
</script>
