from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
import sys
import re
from datetime import datetime

# Check if running in production (on Render)
on_render = os.getenv('RENDER') == 'true'

app = Flask(__name__)

# Database configuration
database_url = os.getenv('DATABASE_URL', 'sqlite:///inventory.db')
if database_url.startswith('postgres://'):
    database_url = database_url.replace('postgres://', 'postgresql://', 1)
app.config['SQLALCHEMY_DATABASE_URI'] = database_url

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    position = db.Column(db.Integer, default=0)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'position': self.position
        }

with app.app_context():
    db.create_all()
    # Add some sample data if the database is empty
    if not Product.query.first():
        sample_products = [
            Product(name='Laptop', price=999.99, description='High performance laptop', position=1),
            Product(name='Mouse', price=29.99, description='Wireless mouse', position=2),
            Product(name='Keyboard', price=59.99, description='Mechanical keyboard', position=3)
        ]
        db.session.add_all(sample_products)
        db.session.commit()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/products', methods=['GET'])
def get_products():
    sort_by = request.args.get('sort', 'position')
    order = request.args.get('order', 'asc')
    
    query = Product.query
    
    if sort_by == 'name':
        query = query.order_by(Product.name.asc() if order == 'asc' else Product.name.desc())
    elif sort_by == 'price':
        query = query.order_by(Product.price.asc() if order == 'asc' else Product.price.desc())
    else:  # Default sort by position
        query = query.order_by(Product.position.asc() if order == 'asc' else Product.position.desc())
    
    products = [p.to_dict() for p in query.all()]
    return jsonify(products)

@app.route('/api/products', methods=['POST'])
def add_product():
    data = request.get_json()
    if not data or 'name' not in data or 'price' not in data:
        return jsonify({'error': 'Name and price are required'}), 400
    
    # Get the next position
    max_position = db.session.query(db.func.max(Product.position)).scalar() or 0
    
    product = Product(
        name=data['name'],
        price=float(data['price']),
        description=data.get('description', ''),
        position=max_position + 1
    )
    
    db.session.add(product)
    db.session.commit()
    return jsonify(product.to_dict()), 201

@app.route('/api/products/reorder', methods=['POST'])
def reorder_products():
    data = request.get_json()
    if not data or 'order' not in data:
        return jsonify({'error': 'Order data is required'}), 400
    
    try:
        for idx, product_id in enumerate(data['order'], 1):
            product = Product.query.get(product_id)
            if product:
                product.position = idx
        db.session.commit()
        return jsonify({'status': 'success'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/api/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    try:
        db.session.delete(product)
        db.session.commit()
        return jsonify({'status': 'success'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    # Use 0.0.0.0 to make the server publicly available
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=not on_render)
