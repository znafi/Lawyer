from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from langdetect import detect
import os
from sqlalchemy import or_

app = Flask(__name__, static_folder='frontend/build', static_url_path='/')
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Configure SQLAlchemy
if os.environ.get('RENDER'):
    # Use PostgreSQL in production
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '').replace('postgres://', 'postgresql://')
else:
    # Use SQLite in development
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///legal_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Models
class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    code = db.Column(db.String(2), nullable=False)
    laws = db.relationship('Law', backref='country', lazy=True)

class Law(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    language = db.Column(db.String(2), nullable=False)
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'), nullable=False)
    keywords = db.Column(db.Text, nullable=False)
    source = db.Column(db.Text, nullable=False)
    section = db.Column(db.String(100))
    year = db.Column(db.Integer)

# Routes
@app.route('/')
def serve():
    return app.send_static_file('index.html')

@app.route('/api/countries', methods=['GET'])
def get_countries():
    try:
        countries = Country.query.all()
        print("Found countries:", [c.name for c in countries])  # Debug log
        return jsonify([{
            'id': c.id,
            'name': c.name,
            'code': c.code
        } for c in countries])
    except Exception as e:
        print("Error getting countries:", str(e))  # Debug log
        return jsonify({'error': str(e)}), 500

@app.route('/api/laws/search', methods=['GET'])
def search_laws():
    try:
        country_id = request.args.get('country_id')
        keywords = request.args.get('keywords', '').lower()
        language = request.args.get('language', 'en')
        
        print(f"Search request - country_id: {country_id}, keywords: {keywords}, language: {language}")  # Debug log
        
        if not country_id or not keywords:
            return jsonify({'error': 'Missing required parameters'}), 400
        
        # Split keywords into individual terms
        search_terms = keywords.split()
        print(f"Search terms: {search_terms}")  # Debug log
        
        # Build search conditions
        conditions = []
        for term in search_terms:
            conditions.append(Law.title.ilike(f'%{term}%'))
            conditions.append(Law.content.ilike(f'%{term}%'))
            conditions.append(Law.keywords.ilike(f'%{term}%'))
        
        # Search in both title, content, and keywords fields
        laws = Law.query.filter_by(country_id=country_id, language=language)\
            .filter(or_(*conditions))\
            .all()
        
        print(f"Found {len(laws)} matching laws")  # Debug log
        
        # Sort results by relevance (number of keyword matches)
        def calculate_relevance(law):
            text = (law.title + ' ' + law.content + ' ' + law.keywords).lower()
            return sum(text.count(term) for term in search_terms)
        
        laws.sort(key=calculate_relevance, reverse=True)
        
        results = [{
            'id': law.id,
            'title': law.title,
            'content': law.content,
            'language': law.language,
            'source': law.source,
            'section': law.section,
            'year': law.year
        } for law in laws]
        
        print(f"Returning {len(results)} results")  # Debug log
        return jsonify(results)
    except Exception as e:
        print("Error in search:", str(e))  # Debug log
        return jsonify({'error': str(e)}), 500

@app.route('/api/languages', methods=['GET'])
def get_languages():
    languages = [
        {'code': 'en', 'name': 'English'},
        {'code': 'es', 'name': 'Spanish'},
        {'code': 'fr', 'name': 'French'},
        {'code': 'de', 'name': 'German'},
        {'code': 'zh', 'name': 'Chinese'},
        {'code': 'ar', 'name': 'Arabic'}
    ]
    return jsonify(languages)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
