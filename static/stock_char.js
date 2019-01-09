
        var ctx = document.getElementById("stockChart").getContext('2d');
        var myChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: [
                    {% for item in labels %}
                        "{{ item }}",
                    {% endfor %}
                ],
                datasets: [{
                    label: '# of Votes',
                    data: [
                        {% for item in values %}
                            {{ item }},
                        {% endfor %}],
                    fill:false,

                    {#backgroundColor: [#}
                    {#    'rgba(40, 180, 99, 0.2)'#}
                    {#],#}
                    borderColor: [
                        'rgba(40, 180, 99, 1.0)',
                    ],
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero: false
                        }
                    }],
                    xAxes: [{
                        gridLines:{
                            display:false
                        }
                    }]
                },



                elements: {
                    point: {
                        radius: 0.4
                    },
                    line: {
                        tension: 0, // disables bezier curves
                    }

                }


            }
        });