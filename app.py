<!DOCTYPE html>
<html>
<head>
    <title>회로 시뮬레이션 시각화 웹 앱</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        body { font-family: sans-serif; padding: 20px; }
        .chart-container { width: 80%; margin: 20px 0; }
    </style>
</head>
<body>
    <h1>🔬 시뮬레이션 결과 대시보드</h1>
    
    <h2>전압 파형 (Voltage)</h2>
    <div class="chart-container">
        <canvas id="voltageChart"></canvas>
    </div>

    <h2>전류 파형 (Current)</h2>
    <div class="chart-container">
        <canvas id="currentChart"></canvas>
    </div>

    <script>
        // Flask 백엔드에서 전달된 JSON 데이터를 파이썬 템플릿 문법으로 받음
        const labels = {{ chart_data.labels | tojson }};
        const voltageData = {{ chart_data.voltage_data | tojson }};
        const currentData = {{ chart_data.current_data | tojson }};

        // 1. 전압(Voltage) 그래프 그리기
        const vtx = document.getElementById('voltageChart').getContext('2d');
        new Chart(vtx, {
            type: 'line',
            data: {
                labels: labels,
                datasets: [{
                    label: '전압 (V)',
                    data: voltageData,
                    borderColor: 'rgb(75, 192, 192)',
                    tension: 0.2, 
                    fill: false
                }]
            },
            options: {
                responsive: true,
                scales: { y: { beginAtZero: false, title: { display: true, text: '전압 (V)' } } }
            }
        });

        // 2. 전류(Current) 그래프 그리기
        const ctx = document.getElementById('currentChart').getContext('2d');
        new Chart(ctx, {
            type: 'line',
            data: {
                labels: labels,
                datasets: [{
                    label: '전류 (A)',
                    data: currentData,
                    borderColor: 'rgb(255, 99, 132)',
                    tension: 0.2, 
                    fill: false
                }]
            },
            options: {
                responsive: true,
                scales: { y: { beginAtZero: true, title: { display: true, text: '전류 (A)' } } }
            }
        });
    </script>
</body>
</html>
