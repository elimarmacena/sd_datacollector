
<template>
  <div>
    <b-container fluid>
      <b-row class="my-1">
        <b-col sm="2" lg="1">
          <label for="Temperature">Temperatura:</label>
        </b-col>
        <b-col sm="2" lg="1">
          <b-form-input id="Temperature" type="number"></b-form-input>
        </b-col>
      </b-row>
      <b-button v-on:click="searchData">Pesquisar</b-button>
    </b-container>
    <div class="row">
      <chartsPlot></chartsPlot>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'TemperatureForm',
  methods: {
    searchData: function () {
      // const temperature_user = document.querySelector('#Temperature').value
      axios
        .get('http://localhost:5000/bytemperature?minTemp=-16&maxTemp=2')
        .then(response => {
          console.log(response.data)
        })
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
