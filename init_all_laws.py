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
        # Criminal Law Section
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
        # Family Law Section
        {
            "title": "Family Law Act - Marriage and Divorce",
            "content": """Family Law Regulations in Canada:

1. Marriage Requirements:
- Minimum age of 18 (or 16 with parental consent)
- Both parties must give free and enlightened consent
- Cannot be closely related by blood or adoption
- Neither party can be currently married

2. Divorce Grounds:
- One year separation
- Adultery
- Physical or mental cruelty

3. Division of Property:
- Equal division of family property
- Exclusion of inherited property
- Special treatment of matrimonial home

4. Child Custody:
- Best interests of the child principle
- Joint or sole custody options
- Access and visitation rights
- Child support obligations""",
            "language": "en",
            "country_id": country_id,
            "keywords": "family law, marriage, divorce, custody, child support",
            "source": "Family Law Act",
            "section": "Marriage and Divorce",
            "year": 2023
        },
        # Property Law
        {
            "title": "Property Law - Real Estate",
            "content": """Real Estate Law in Canada:

1. Property Ownership:
- Freehold ownership
- Leasehold interests
- Condominium ownership
- Joint tenancy vs tenancy in common

2. Property Transfer:
- Land registration requirements
- Title search process
- Transfer documentation
- Property taxes

3. Landlord-Tenant Relations:
- Lease requirements
- Tenant rights
- Landlord obligations
- Eviction procedures

4. Zoning and Land Use:
- Municipal zoning bylaws
- Building permits
- Environmental regulations
- Heritage property rules""",
            "language": "en",
            "country_id": country_id,
            "keywords": "property law, real estate, land ownership, landlord, tenant",
            "source": "Property Law Act",
            "section": "Real Estate",
            "year": 2023
        },
        # Immigration Law
        {
            "title": "Immigration and Refugee Protection Act",
            "content": """Immigration Laws in Canada:

1. Immigration Categories:
- Economic Class
- Family Class
- Refugee Class
- Temporary Residents

2. Permanent Residence:
- Points system requirements
- Processing procedures
- Rights and obligations
- Path to citizenship

3. Temporary Status:
- Student visas
- Work permits
- Visitor visas
- Extension procedures

4. Refugee Protection:
- Refugee claim process
- Safe third country agreement
- Appeal procedures
- Protected person status""",
            "language": "en",
            "country_id": country_id,
            "keywords": "immigration, refugee, permanent residence, citizenship",
            "source": "Immigration and Refugee Protection Act",
            "section": "General Provisions",
            "year": 2023
        },
        # Business Law
        {
            "title": "Business Corporations Act",
            "content": """Business Law in Canada:

1. Corporation Formation:
- Registration requirements
- Types of corporations
- Articles of incorporation
- Corporate bylaws

2. Corporate Governance:
- Directors' duties
- Shareholders' rights
- Annual meetings
- Record keeping

3. Business Operations:
- Contract formation
- Commercial transactions
- Intellectual property
- Employment contracts

4. Corporate Finance:
- Share issuance
- Debt financing
- Financial statements
- Dividend distribution""",
            "language": "en",
            "country_id": country_id,
            "keywords": "business law, corporations, corporate governance, commercial law",
            "source": "Business Corporations Act",
            "section": "Corporate Law",
            "year": 2023
        },
        # Environmental Law
        {
            "title": "Environmental Protection Act",
            "content": """Environmental Laws in Canada:

1. Environmental Assessment:
- Project evaluation
- Impact studies
- Public consultation
- Mitigation measures

2. Pollution Control:
- Air quality standards
- Water protection
- Soil contamination
- Waste management

3. Wildlife Protection:
- Species at risk
- Habitat conservation
- Hunting regulations
- Marine protection

4. Climate Change:
- Emission standards
- Carbon pricing
- Clean energy requirements
- Reporting obligations""",
            "language": "en",
            "country_id": country_id,
            "keywords": "environmental law, pollution, wildlife, climate change",
            "source": "Environmental Protection Act",
            "section": "General Provisions",
            "year": 2023
        }
    ]
    
    for law_data in additional_laws:
        law = Law(**law_data)
        db.session.add(law)

def add_french_translations(country_id):
    french_laws = [
        # Criminal Law in French
        {
            "title": "Code criminel - Principes généraux",
            "content": """Le Code criminel du Canada établit les principes généraux suivants:

1. Présomption d'innocence:
- Toute personne accusée d'une infraction est présumée innocente
- Le fardeau de la preuve incombe à la poursuite
- La preuve doit être hors de tout doute raisonnable

2. Responsabilité criminelle:
- Âge minimum de responsabilité: 12 ans
- Défense de troubles mentaux disponible
- L'intoxication n'est généralement pas une défense""",
            "language": "fr",
            "country_id": country_id,
            "keywords": "code criminel, droit pénal, principes, responsabilité",
            "source": "Code criminel du Canada",
            "section": "Principes généraux",
            "year": 2023
        },
        # Family Law in French
        {
            "title": "Loi sur le droit de la famille - Mariage et divorce",
            "content": """Règlements du droit de la famille au Canada:

1. Exigences du mariage:
- Âge minimum de 18 ans (16 avec consentement parental)
- Consentement libre et éclairé des deux parties
- Absence de liens de parenté proche
- Aucun mariage existant

2. Motifs de divorce:
- Séparation d'un an
- Adultère
- Cruauté physique ou mentale""",
            "language": "fr",
            "country_id": country_id,
            "keywords": "droit famille, mariage, divorce, garde, pension alimentaire",
            "source": "Loi sur le droit de la famille",
            "section": "Mariage et divorce",
            "year": 2023
        },
        # Immigration Law in French
        {
            "title": "Loi sur l'immigration et la protection des réfugiés",
            "content": """Lois sur l'immigration au Canada:

1. Catégories d'immigration:
- Classe économique
- Catégorie familiale
- Catégorie des réfugiés
- Résidents temporaires

2. Résidence permanente:
- Système de points
- Procédures de traitement
- Droits et obligations
- Voie vers la citoyenneté""",
            "language": "fr",
            "country_id": country_id,
            "keywords": "immigration, réfugié, résidence permanente, citoyenneté",
            "source": "Loi sur l'immigration et la protection des réfugiés",
            "section": "Dispositions générales",
            "year": 2023
        }
    ]
    
    for law_data in french_laws:
        law = Law(**law_data)
        db.session.add(law)

if __name__ == "__main__":
    init_all_laws()
