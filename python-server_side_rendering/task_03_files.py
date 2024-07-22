from flask import Flask, render_template, request
import json
import csv


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
   
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    
    with open('items.json', 'r') as f:
        items = json.load(f)

    return render_template('items.html', items=items.get('items', []))

@app.route('/products')
def products():
    source = request.args.get('source')
    id = request.args.get('id')
    
    products = []
    if source == 'json':
        with open('products.json', 'r') as f:
            products = json.load(f)
            
    elif source == 'csv':
        with open('products.csv', 'r') as f:
            data = csv.DictReader(f)
            for row in data:
                products.append(row)
    else:
        return render_template('product_display.html', errorMessage="Wrong source")
    
    if id:
        products = [product for product in products if str(product['id']) == id]

        if len(products) == 0:
                return render_template('product_display.html', errorMessage="Product not found")
    
    return render_template('product_display.html', products=products)
    
if __name__ == '__main__':
    app.run(debug=True, port=5000)