<template>
<div>
  <div class="bg-div" :style="{ background: 'url(' + require('@/assets/control_background.jpg') + ')' }"></div>
    <div class="card-location">
      <b-card title="Relatorio Monitoramento" style="max-width: 55%;background-color: rgba(0,0,0, 0.4); color: white" class="text-center">
      <b-card-text>Solução web para a exibição dos dados disponibilizados através do envio dos devices.<br><br>
      Os dados utilizados para os relatorios são gerados através de um script Python, no intuito de simular a operação de um device de ambiente.<br><br>
      Após o gerados, os dados são enviados para uma fila do rabbitMQ, no qual mantem esses dados até que exista um consumidor para solicita-los,
       alem disso o rabbitMQ oferece a ordenação das mensagens enviadas e não obriga o device aguardar até ficar disponivel para receber as informações.<br><br>
      A solicitação de dados para o relatorio são direcionadas para uma API desenvolvida em Flask, framework de microserviço escrita na linguagem Pythom.
       Esta API acessa o banco com o base no filtro informado e então devolve os dados para a solução Front-End, o atual site.
      </b-card-text>
      </b-card>
    </div>
</div>
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
.bg-div{
  background-color: #000000;
  height: 100vh;
  filter: blur(8px);
  -webkit-filter: blur(8px)
  }
.content-space{
  font-size: 30px;
  background-color: rgb(0,0,0); /* Fallback color */
  background-color: rgba(0,0,0, 0.4); /* Black w/opacity/see-through */
  color: #FFFFFF;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 2;
  width: 90%;
  padding: 20px;
  text-align: center;
  font-family: fantasy;
}
.content-space p{
  text-align: justify
}
.card-location{
  position: absolute;
  top: 10%;
  left: 28%
}
</style>
