from app import app, db, Country, Law
from add_canadian_constitution import add_canadian_constitution
from add_canadian_common_laws import add_canadian_common_laws
from add_detailed_traffic_laws import add_traffic_laws

def init_all_laws():
    print("Starting law initialization...")
    with app.app_context():
        try:
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
            
            # Add all types of laws
            print("Adding constitutional laws...")
            add_canadian_constitution()
            
            print("Adding common laws...")
            add_canadian_common_laws()
            
            print("Adding traffic laws...")
            add_traffic_laws()
            
            # Add additional laws
            print("Adding additional laws...")
            add_additional_laws(canada.id)
            
            # Add French translations
            print("Adding French translations...")
            add_french_translations(canada.id)
            
            db.session.commit()
            print("Law initialization complete!")
            
        except Exception as e:
            print(f"Error during law initialization: {str(e)}")
            db.session.rollback()
            raise

def add_additional_laws(country_id):
    additional_laws = [
        {
            "title": "Criminal Code - General Principles",
            "content": """The Criminal Code of Canada establishes the following general principles:

1. Presumption of Innocence:
- Everyone charged with an offense is presumed innocent until proven guilty
- The burden of proof lies with the prosecution
- Proof must be beyond reasonable doubt

2. Criminal Responsibility:
- Minimum age of criminal responsibility is 12 years
- Mental disorder defense available when applicable
- Intoxication generally not a defense

3. Jurisdiction:
- Applies throughout Canada
- Some provisions have extraterritorial reach
- Covers acts on aircraft and ships""",
            "language": "en",
            "country_id": country_id,
            "keywords": "criminal code, criminal law, principles, responsibility",
            "source": "Criminal Code of Canada",
            "section": "General Principles",
            "year": 2023
        },
        {
            "title": "Employment Standards",
            "content": """Key Employment Standards in Canada:

1. Minimum Wage:
- Varies by province/territory
- Regular reviews and adjustments
- Special rates for certain categories

2. Working Hours:
- Standard work week: 40 hours
- Overtime pay after 44 hours
- Minimum rest periods required

3. Vacation and Leave:
- Minimum 2 weeks paid vacation
- Statutory holidays
- Various types of leave (medical, family, etc.)

4. Termination Notice:
- Required notice periods
- Severance pay requirements
- Exceptions for cause""",
            "language": "en",
            "country_id": country_id,
            "keywords": "employment, labor law, workers rights, minimum wage",
            "source": "Employment Standards Act",
            "section": "Basic Standards",
            "year": 2023
        }
    ]
    
    for law_data in additional_laws:
        law = Law(**law_data)
        db.session.add(law)

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
        },
        {
            "title": "Code criminel - Principes généraux",
            "content": """Le Code criminel du Canada établit les principes généraux suivants:

1. Présomption d'innocence:
- Toute personne accusée d'une infraction est présumée innocente jusqu'à preuve du contraire
- Le fardeau de la preuve incombe à la poursuite
- La preuve doit être établie hors de tout doute raisonnable

2. Responsabilité criminelle:
- L'âge minimum de la responsabilité criminelle est de 12 ans
- La défense de troubles mentaux est disponible le cas échéant
- L'intoxication n'est généralement pas une défense""",
            "language": "fr",
            "country_id": country_id,
            "keywords": "code criminel, droit pénal, principes, responsabilité",
            "source": "Code criminel du Canada",
            "section": "Principes généraux",
            "year": 2023
        },
        {
            "title": "Normes d'emploi",
            "content": """Normes d'emploi principales au Canada:

1. Salaire minimum:
- Varie selon la province/territoire
- Révisions et ajustements réguliers
- Taux spéciaux pour certaines catégories

2. Heures de travail:
- Semaine normale: 40 heures
- Heures supplémentaires après 44 heures
- Périodes de repos minimales requises""",
            "language": "fr",
            "country_id": country_id,
            "keywords": "emploi, droit du travail, droits des travailleurs, salaire minimum",
            "source": "Loi sur les normes d'emploi",
            "section": "Normes de base",
            "year": 2023
        }
    ]
    
    for law_data in french_laws:
        law = Law(**law_data)
        db.session.add(law)

if __name__ == "__main__":
    init_all_laws()
