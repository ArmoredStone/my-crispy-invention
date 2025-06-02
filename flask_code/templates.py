from typing import Final

# HTML template for rendering transactions
TRANSACTIONS_TEMPLATE: Final = """
<!DOCTYPE html>
<html>
<head>
    <title>Transactions</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        table { border-collapse: collapse; width: 100%; margin-bottom: 20px; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        th { background-color: #f2f2f2; }
        tr:nth-child(even) { background-color: #f9f9f9; }
        tr:hover { background-color: #f5f5f5; }
        .result-image { max-width: 200px; max-height: 200px; object-fit: contain; }
        
        /* Pagination styles */
        .pagination {
            display: flex;
            justify-content: center;
            gap: 10px;
            margin: 20px 0;
        }
        .pagination a, .pagination span {
            padding: 8px 16px;
            text-decoration: none;
            border: 1px solid #ddd;
            border-radius: 4px;
            color: #333;
        }
        .pagination a:hover {
            background-color: #f2f2f2;
        }
        .pagination .current {
            background-color: #4CAF50;
            color: white;
            border-color: #4CAF50;
        }
        .pagination .disabled {
            color: #999;
            pointer-events: none;
        }
        .page-size-selector {
            margin: 20px 0;
            text-align: right;
        }
        .page-size-selector select {
            padding: 5px;
            border-radius: 4px;
            border: 1px solid #ddd;
        }
        .page-size-selector label {
            margin-right: 10px;
        }
    </style>
</head>
<body>
    <h1>Transactions</h1>
    
    <div class="page-size-selector">
        <label for="page-size">Items per page:</label>
        <select id="page-size" onchange="changePageSize(this.value)">
            {% for size in allowed_page_sizes %}
            <option value="{{ size }}" {% if size == page_size %}selected{% endif %}>{{ size }}</option>
            {% endfor %}
        </select>
    </div>

    <table>
        <tr>
            <th>ID</th>
            <th>Author</th>
            <th>Prompt</th>
            <th>Revised Prompt</th>
            <th>Image URL</th>
            <th>Created At</th>
        </tr>
        {% for transaction in transactions %}
        <tr>
            <td>{{ transaction.id }}</td>
            <td>{{ transaction.author }}</td>
            <td>{{ transaction.prompt }}</td>
            <td>{{ transaction.revised_prompt }}</td>
            <td><img src="{{ transaction.result_image_url }}" alt="Generated image" class="result-image"></td>
            <td>{{ transaction.created_at }}</td>
        </tr>
        {% endfor %}
    </table>

    <div class="pagination">
        {% if current_page > 1 %}
            <a href="?page=1&page_size={{ page_size }}">&laquo; First</a>
            <a href="?page={{ current_page - 1 }}&page_size={{ page_size }}">&lsaquo; Previous</a>
        {% else %}
            <span class="disabled">&laquo; First</span>
            <span class="disabled">&lsaquo; Previous</span>
        {% endif %}

        <span class="current">Page {{ current_page }} of {{ total_pages }}</span>

        {% if current_page < total_pages %}
            <a href="?page={{ current_page + 1 }}&page_size={{ page_size }}">Next &rsaquo;</a>
            <a href="?page={{ total_pages }}&page_size={{ page_size }}">Last &raquo;</a>
        {% else %}
            <span class="disabled">Next &rsaquo;</span>
            <span class="disabled">Last &raquo;</span>
        {% endif %}
    </div>

    <script>
        function changePageSize(size) {
            window.location.href = `?page=1&page_size=${size}`;
        }
    </script>
</body>
</html>
"""