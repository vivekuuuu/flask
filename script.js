document.addEventListener('DOMContentLoaded', function() {
    const ctx = document.getElementById('expenseChart').getContext('2d');
    const expenses = { expenses, tojson };
    const categories = {};
    
    expenses.forEach(expense => {
        if (categories[expense[3]]) {
            categories[expense[3]] += expense[2];
        } else {
            categories[expense[3]] = expense[2];
        }
    });

    const data = {
        labels: Object.keys(categories),
        datasets: [{
            label: 'Expenses',
            data: Object.values(categories),
            backgroundColor: ['#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF', '#FF9F40']
        }]
    };

    new Chart(ctx, {
        type: 'pie',
        data: data
    });
});