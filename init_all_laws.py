from app import app, db, Country, Law
from add_canadian_constitution import add_canadian_constitution
from add_canadian_common_laws import add_canadian_common_laws
from add_detailed_traffic_laws import add_traffic_laws

def init_all_laws():
    print("Starting law initialization...")
    with app.app_context():
        # First, ensure we have the country
        canada = Country.query.filter_by(code="CA").first()
        if not canada:
            print("Creating Canada in database...")
            canada = Country(name='Canada', code='CA')
            db.session.add(canada)
            db.session.commit()
        
        # Clear existing laws if any
        print("Clearing existing laws...")
        Law.query.delete()
        db.session.commit()
        
        print("Adding constitutional laws...")
        add_canadian_constitution()
        
        print("Adding common laws...")
        add_canadian_common_laws()
        
        print("Adding traffic laws...")
        add_traffic_laws()
        
        # Add French translations for some key laws
        print("Adding French translations...")
        add_french_translations(canada.id)
        
        db.session.commit()
        print("Law initialization complete!")

def add_french_translations(country_id):
    french_laws = [
        {
            "title": "Charte canadienne des droits et libertés",
            "content": """La Charte canadienne des droits et libertés garantit les droits et libertés qui y sont énoncés. Ils ne peuvent être restreints que par une règle de droit, dans des limites qui soient raisonnables et dont la justification puisse se démontrer dans le cadre d'une société libre et démocratique.

Libertés fondamentales:
Chacun a les libertés fondamentales suivantes:
a) liberté de conscience et de religion;
b) liberté de pensée, de croyance, d'opinion et d'expression, y compris la liberté de la presse et des autres moyens de communication;
c) liberté de réunion pacifique;
d) liberté d'association.""",
            "language": "fr",
            "country_id": country_id,
            "keywords": "charte, droits, libertés, libertés fondamentales, droits démocratiques",
            "source": "Loi constitutionnelle de 1982",
            "section": "Partie I",
            "year": 1982
        },
        {
            "title": "Code de la route - Règles générales",
            "content": """Règles générales de circulation:
1. Tout conducteur doit:
- Respecter les limites de vitesse
- S'arrêter aux feux rouges et aux panneaux d'arrêt
- Céder le passage aux piétons
- Porter une ceinture de sécurité

2. Infractions et pénalités:
- Excès de vitesse
- Conduite dangereuse
- Conduite avec facultés affaiblies""",
            "language": "fr",
            "country_id": country_id,
            "keywords": "circulation, code de la route, règles, infractions",
            "source": "Code de la route",
            "section": "Règles générales",
            "year": 2023
        }
    ]
    
    for law_data in french_laws:
        law = Law(**law_data)
        db.session.add(law)

if __name__ == "__main__":
    init_all_laws()
