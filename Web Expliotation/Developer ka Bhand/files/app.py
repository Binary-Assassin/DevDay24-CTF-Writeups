from flask import Flask, render_template_string

app = Flask(__name__)

html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>E-commerce Store</title>
    <style>
        /* Reset styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            color: #333;
            line-height: 1.6;
        }

        header {
            background-color: #333;
            color: #fff;
            padding: 1rem;
            text-align: center;
        }

        header h1 {
            margin-bottom: 0.5rem;
        }

        nav ul {
            list-style: none;
        }

        nav ul li {
            display: inline;
            margin-right: 1rem;
        }

        nav ul li a {
            color: #fff;
            text-decoration: none;
        }

        main {
            display: flex;
            flex-wrap: wrap;
            justify-content: space-around;
            padding: 2rem;
        }

        .product {
            background-color: #fff;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
            padding: 1.5rem;
            margin-bottom: 2rem;
            width: calc(25% - 2rem); /* 25% width with some margin */
            margin-right: 2rem;
            margin-left: 2rem;
        }

        .product img {
            max-width: 100%;
            height: auto;
        }

        .product h2 {
            margin-top: 1rem;
        }

        .product .price {
            font-weight: bold;
        }

        .product button {
            display: block;
            width: 100%;
            padding: 0.5rem;
            background-color: #333;
            color: #fff;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            margin-top: 1rem;
        }

        .product button:hover {
            background-color: #555;
        }

        footer {
            background-color: #333;
            color: #fff;
            text-align: center;
            padding: 1rem;
            position: fixed;
            bottom: 0;
            width: 100%;
        }
    </style>
</head>
<body>
    <header>
        <h1>E-commerce Store</h1>
        <nav>
            <ul>
                <li><a href="#">Home</a></li>
                <li><a href="#">Shop</a></li>
                <li><a href="#">About</a></li>
                <li><a href="#">Contact</a></li>
            </ul>
        </nav>
    </header>
    
    <main>
        <section class="product">
            <img src="{{ url_for('static', filename='1.jpg') }}" alt="Product 1">
            <h2>Product 1</h2>
            <p class="price">$19.99</p>
            <button>Add to Cart</button>
        </section>

        <section class="product">
            <img src="{{ url_for('static', filename='2.jpg') }}" alt="Product 2">
            <h2>Product 2</h2>
            <p class="price">$24.99</p>
            <button>Add to Cart</button>
        </section>

        <section class="product">
            <img src="{{ url_for('static', filename='3.jpeg') }}" alt="Product 3">
            <h2>Product 3</h2>
            <p class="price">$29.99</p>
            <button>Add to Cart</button>
        </section>

        <section class="product">
            <img src="{{ url_for('static', filename='4.jpeg') }}" alt="Product 4">
            <h2>Product 4</h2>
            <p class="price">$34.99</p>
            <button>Add to Cart</button>
        </section>

        <section class="product">
            <img src="{{ url_for('static', filename='5.jpeg') }}" alt="Product 5">
            <h2>Product 5</h2>
            <p class="price">$39.99</p>
            <button>Add to Cart</button>
        </section>

        <section class="product">
            <img src="{{ url_for('static', filename='6.jpeg') }}" alt="Product 6">
            <h2>Product 6</h2>
            <p class="price">$44.99</p>
            <button>Add to Cart</button>
        </section>
        
    <footer>
        <p>&copy; 2024 E-commerce Store. All rights reserved.</p>
    </footer>
    <!-- Admin Credentials for Testing Environment --> 
    <!-- Admin Credentials: username=admin, password=DD24{Html_c0mM3nT5} -->
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
