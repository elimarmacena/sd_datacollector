import {Line} from 'vue-chartjs'

export default Line.extend ( {
    mounted () {
        this.renderChart({
            label: ['1','2','3'],
            datasets: [
                {label: 'my activities', backdropColor: '#dd4b39', data: [4,5,6]}
            ]
        })
    }
})
