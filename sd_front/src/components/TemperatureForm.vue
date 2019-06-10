
<template>
  <div>
    <b-container fluid>
      <b-row class="my-1">
        <b-col sm="2" lg="1">
          <label for="minTemperature">Temperatura Minima:</label>
        </b-col>
        <b-col sm="2" lg="1">
          <b-form-input id="minTemperature" type="number"></b-form-input>
        </b-col>
      </b-row>
      <b-row class="my-1">
        <b-col sm="2" lg="1">
          <label for="maxTemperature">Temperatura Maxima:</label>
        </b-col>
        <b-col sm="2" lg="1">
          <b-form-input id="maxTemperature" type="number"></b-form-input>
        </b-col>
      </b-row>
      <b-button v-on:click="searchData">Pesquisar</b-button>
    </b-container>
    <div>
      <chart :options="teste"></chart>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'TemperatureForm',
  data: () => ({
    chartOptionsBar: {
      xAxis: { data: ['Q1', 'Q2', 'Q3', 'Q4'] },
      yAxis: { type: 'value' },
      series: [{ type: 'bar', data: [63, 75, 24, 92] }]
    },
    teste: {}
  }),
  methods: {
    searchData: function () {
      const MinUser = document.querySelector('#minTemperature').value
      const MaxUser = document.querySelector('#maxTemperature').value
      var ResultRequest = null
      axios
        .get('http://localhost:5000/bytemperature?minTemp=' + MinUser + '&maxTemp=' + MaxUser)
        .then(response => {
          // var ownerList = response.data.map(a => a.owner)
          // let unicOwner = ownerList.filter((v, i) => ownerList.indexOf(v) === i)
          // let dateList = response.data.map(a => a.send_data)
          // let temperature = response.data.map(a => a.temperature)
          console.log(response.data)
        })
      console.log(ResultRequest)
      this.teste = this.chartOptionsBar
    }
  }
}
</script>
