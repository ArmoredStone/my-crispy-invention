from typing import Final

# HTML template for rendering transactions
TRANSACTIONS_TEMPLATE: Final = """
<!DOCTYPE html>
<html>
<head>
    <title>Transactions</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        table { border-collapse: collapse; width: 100%; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        th { background-color: #f2f2f2; }
        tr:nth-child(even) { background-color: #f9f9f9; }
        tr:hover { background-color: #f5f5f5; }
    </style>
</head>
<body>
    <h1>Transactions</h1>
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
            <td><a href="{{ transaction.result_image_url }}" target="_blank">View Image</a></td>
            <td>{{ transaction.created_at }}</td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
"""