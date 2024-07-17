from flask import Flask, render_template
import json


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
    try:
    
        with open('items.json', 'r') as f:
            items = json.load(f)
            
        values = items.get('items', [])
    except Exception:
        values = []
        
    return render_template('items.html', values=values)

if __name__ == '__main__':
    app.run(debug=True, port=5000)