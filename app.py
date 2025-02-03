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
    database_url = os.environ.get('DATABASE_URL')
    if database_url:
        # Render provides PostgreSQL URLs starting with postgres://, but SQLAlchemy requires postgresql://
        database_url = database_url.replace('postgres://', 'postgresql://')
    else:
        # Fallback to SQLite if no DATABASE_URL is set
        database_url = 'sqlite:///legal_database.db'
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url
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

def init_database():
    with app.app_context():
        # Create all tables
        db.create_all()
        
        try:
            # Import and run the comprehensive law initialization
            from init_all_laws import init_all_laws
            init_all_laws()
        except Exception as e:
            print(f"Error initializing laws: {str(e)}")
            # If comprehensive initialization fails, add basic data
            if Country.query.count() == 0:
                canada = Country(name='Canada', code='CA')
                db.session.add(canada)
                db.session.commit()

                law1 = Law(
                    title='Constitution Act, 1867',
                    content='The Constitution Act, 1867 is a major part of Canada\'s Constitution...',
                    language='en',
                    country_id=canada.id,
                    keywords='constitution,fundamental law,confederation',
                    source='Government of Canada',
                    section='Constitution',
                    year=1867
                )
                
                law2 = Law(
                    title='Loi constitutionnelle de 1867',
                    content='La Loi constitutionnelle de 1867 est une partie majeure de la Constitution du Canada...',
                    language='fr',
                    country_id=canada.id,
                    keywords='constitution,loi fondamentale,confédération',
                    source='Gouvernement du Canada',
                    section='Constitution',
                    year=1867
                )
                
                db.session.add_all([law1, law2])
                db.session.commit()

# Initialize database
init_database()

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
    print("Languages endpoint called")  # Debug log
    try:
        # Query distinct languages from the database
        languages = db.session.query(Law.language).distinct().all()
        print(f"Found languages in DB: {languages}")  # Debug log
        
        # Convert to list of language codes
        language_list = [lang[0] for lang in languages]
        print(f"Language list: {language_list}")  # Debug log
        
        # If no languages found, return default languages
        if not language_list:
            print("No languages found, using defaults")  # Debug log
            language_list = ['en', 'fr']
            
        # Map language codes to full names
        language_names = {
            'en': 'English',
            'fr': 'French',
            # Add more languages as needed
        }
        
        # Format response
        response = [
            {'code': code, 'name': language_names.get(code, code)}
            for code in language_list
        ]
        
        print(f"Sending response: {response}")  # Debug log
        return jsonify(response)
    except Exception as e:
        print(f"Error getting languages: {str(e)}")  # Debug log
        return jsonify([
            {'code': 'en', 'name': 'English'},
            {'code': 'fr', 'name': 'French'}
        ])

if __name__ == '__main__':
    app.run(debug=True)
