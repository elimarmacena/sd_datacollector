<template>
  <div>
    <div>
      <b-navbar toggleable="lg" type="light" variant="info">
        <b-navbar-brand>TIpo de Busca</b-navbar-brand>
        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
        <b-collapse id="nav-collapse" is-nav>
          <b-navbar-nav>
            <b-nav-item href="/#/ownerForm">Produtor</b-nav-item>
            <b-nav-item>/</b-nav-item>
            <b-nav-item href="/#/intervalDaysForm">Intervalo de Tempo</b-nav-item>
          </b-navbar-nav>
          <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
        </b-collapse>
      </b-navbar>
    </div>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
