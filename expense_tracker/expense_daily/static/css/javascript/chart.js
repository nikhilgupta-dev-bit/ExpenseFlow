const ctx = document.getElementById('expenseChart').getContext('2d');
const expenseChart = new Chart(ctx, {
    type: 'pie',
    data: {
        labels: [], // Set this dynamically in your HTML template
        datasets: [{
            data: [], // Set this dynamically in your HTML template
            backgroundColor: [
                '#007bff', '#ffc107', '#dc3545', '#28a745', '#6f42c1', '#fd7e14', '#20c997', '#17a2b8'
            ],
            borderWidth: 1
        }]
    },
    options: {
        responsive: false, // important!
        plugins: {
            legend: {
                position: 'bottom'
            },
            title: {
                display: true,
                text: 'Expenses by Category'
            }
        }
    }
});
