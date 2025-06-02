from typing import Final

CREATE_TRANSACTION_TEMPLATE: Final = """
<!DOCTYPE html>
<html>
<head>
    <title>Create Transaction</title>
    <style>
        body { 
            font-family: Arial, sans-serif; 
            margin: 20px;
            max-width: 800px;
            margin: 20px auto;
            padding: 0 20px;
        }
        .form-container {
            background-color: #f9f9f9;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .form-group {
            margin-bottom: 20px;
        }
        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
            color: #333;
        }
        input[type="text"], textarea {
            width: 100%;
            padding: 8px;
            border: 1px solid #ddd;
            border-radius: 4px;
            box-sizing: border-box;
            font-size: 14px;
        }
        textarea {
            min-height: 100px;
            resize: vertical;
        }
        button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
        }
        button:hover {
            background-color: #45a049;
        }
        .error {
            color: #ff0000;
            margin-top: 5px;
            font-size: 14px;
        }
        .success {
            color: #4CAF50;
            margin-top: 5px;
            font-size: 14px;
        }
        .back-link {
            display: inline-block;
            margin-bottom: 20px;
            color: #666;
            text-decoration: none;
        }
        .back-link:hover {
            color: #333;
        }
    </style>
</head>
<body>
    <a href="/list" class="back-link">&larr; Back to Transactions</a>
    <h1>Create New Transaction</h1>
    
    <div class="form-container">
        <form id="createTransactionForm" onsubmit="handleSubmit(event)">
            <div class="form-group">
                <label for="author">Author:</label>
                <input type="text" id="author" name="author" required>
            </div>
            
            <div class="form-group">
                <label for="prompt">Prompt:</label>
                <textarea id="prompt" name="prompt" required></textarea>
            </div>
            
            <button type="submit">Create Transaction</button>
        </form>
        <div id="message"></div>
    </div>

    <script>
        async function handleSubmit(event) {
            event.preventDefault();
            
            const form = event.target;
            const messageDiv = document.getElementById('message');
            
            const formData = {
                author: form.author.value.trim(),
                prompt: form.prompt.value.trim()
            };

            try {
                const response = await fetch('/api/create_transaction', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(formData)
                });

                if (response.ok) {
                    messageDiv.className = 'success';
                    messageDiv.textContent = 'Transaction completed successfully!';
                    form.reset();
                    // Redirect to transactions page after 2 seconds
                    setTimeout(() => {
                        window.location.href = '/list';
                    }, 3000);
                } else {
                    const error = await response.json();
                    messageDiv.className = 'error';
                    messageDiv.textContent = error.message || 'Failed to create transaction';
                }
            } catch (error) {
                messageDiv.className = 'error';
                messageDiv.textContent = 'An error occurred while creating the transaction';
            }
        }
    </script>
</body>
</html>
"""

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
    <a href="/create" class="create-link">Create New Transaction</a>
    
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