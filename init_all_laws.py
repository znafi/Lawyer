from app import app, db, Country, Law
from add_canadian_constitution import add_canadian_constitution
from add_canadian_common_laws import add_canadian_common_laws
from add_detailed_traffic_laws import add_detailed_traffic_laws

def init_all_laws():
    with app.app_context():
        # Reset database
        db.drop_all()
        db.create_all()
        
        # Add Canada
        canada = Country(name='Canada', code='CA')
        db.session.add(canada)
        db.session.commit()
        
        # Add laws
        add_canadian_constitution()
        add_canadian_common_laws()
        add_detailed_traffic_laws(canada.id)
        add_additional_laws(canada.id)
        add_french_translations(canada.id)
        
        # Add additional laws
        print("Adding additional laws...")
        add_additional_laws(canada.id)
        
        # Add French translations
        print("Adding French translations...")
        add_french_translations(canada.id)
        
        db.session.commit()
        print("Law initialization complete!")
            
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
        },
        # DUI and Impaired Driving Laws
        {
            "title": "Impaired Driving and DUI Laws",
            "content": """Drinking and Driving Laws in Canada:

1. Blood Alcohol Concentration (BAC) Limits:
- 0.08% (80mg/100ml) - Criminal Code limit
- 0.05% to 0.079% - Provincial administrative penalties
- Zero tolerance for new drivers
- Zero tolerance for commercial drivers

2. Penalties for DUI/Impaired Driving:
First Offense:
- Minimum $1000 fine
- Mandatory driving prohibition (1-3 years)
- Criminal record
- Mandatory education program
- Possible jail time (up to 10 years for dangerous driving)

Second Offense:
- Minimum 30 days imprisonment
- Longer driving prohibition
- Mandatory alcohol ignition interlock

Additional Penalties:
- Vehicle impoundment
- License suspension
- Insurance rate increase
- Border crossing restrictions

3. Types of Impaired Driving:
- Alcohol impairment
- Drug impairment (including cannabis)
- Combined alcohol and drug impairment
- Driving while fatigued

4. Testing and Evidence:
- Breathalyzer tests
- Field sobriety tests
- Drug recognition evaluation
- Blood tests
- Refusal to provide sample (criminal offense)

5. Legal Rights During DUI Stop:
- Right to remain silent
- Right to legal counsel
- Right to know the reason for stop
- Right to second breath test""",
            "language": "en",
            "country_id": country_id,
            "keywords": "DUI, drunk driving, impaired driving, drinking and driving, BAC, blood alcohol, breathalyzer, RIDE program, license suspension, criminal code, driving under influence, alcohol, cannabis, drugs, driving prohibition, vehicle impoundment, drunk, intoxicated driving, DWI, over 80, refuse breath sample",
            "source": "Criminal Code of Canada, Highway Traffic Act",
            "section": "Impaired Driving Offenses",
            "year": 2023
        },
        # Traffic Violations and Penalties
        {
            "title": "Traffic Violations and Penalties",
            "content": """Traffic Violations in Canada:

1. Moving Violations:
- Speeding tickets
- Running red lights
- Illegal turns
- Failure to yield
- Following too closely
- Careless driving
- Racing/Stunt driving
- Distracted driving
- Driving without insurance
- Driving while suspended

2. Demerit Point System:
- Point accumulation periods
- License suspension thresholds
- Insurance impact
- Point removal process

3. Fines and Penalties:
- Graduated fine system
- Court appearances
- License suspensions
- Vehicle impoundment
- Insurance implications

4. Administrative Penalties:
- Immediate roadside suspensions
- Vehicle seizures
- Administrative driving prohibitions
- Mandatory driver improvement programs""",
            "language": "en",
            "country_id": country_id,
            "keywords": "traffic ticket, speeding ticket, running red light, illegal turn, yield, careless driving, racing, stunt driving, distracted driving, no insurance, suspended license, demerit points, traffic court, traffic violation, driving offense, traffic fine, traffic penalty, driving prohibition, license suspension",
            "source": "Highway Traffic Act",
            "section": "Traffic Violations",
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
        },
        # DUI Laws in French
        {
            "title": "Lois sur la conduite avec facultés affaiblies",
            "content": """Lois sur l'alcool au volant au Canada:

1. Limites d'alcoolémie:
- 0,08 % (80mg/100ml) - Limite du Code criminel
- 0,05 % à 0,079 % - Sanctions administratives provinciales
- Tolérance zéro pour les nouveaux conducteurs
- Tolérance zéro pour les conducteurs commerciaux

2. Sanctions pour conduite avec facultés affaiblies:
Première infraction:
- Amende minimale de 1000 $
- Interdiction de conduire obligatoire (1-3 ans)
- Casier judiciaire
- Programme de formation obligatoire

Deuxième infraction:
- Emprisonnement minimum de 30 jours
- Interdiction de conduire prolongée
- Antidémarreur éthylométrique obligatoire""",
            "language": "fr",
            "country_id": country_id,
            "keywords": "conduite avec facultés affaiblies, alcool au volant, ivresse au volant, alcoolémie, éthylotest, suspension de permis, code criminel, cannabis, drogues, interdiction de conduire, saisie de véhicule, conduite en état d'ébriété",
            "source": "Code criminel du Canada, Code de la route",
            "section": "Infractions de conduite avec facultés affaiblies",
            "year": 2023
        },
        # Traffic Violations in French
        {
            "title": "Infractions routières et pénalités",
            "content": """Infractions routières au Canada:

1. Infractions mobiles:
- Excès de vitesse
- Feux rouges grillés
- Virages illégaux
- Omission de céder le passage
- Suivre de trop près
- Conduite imprudente
- Course/Conduite dangereuse
- Conduite distraite

2. Système de points d'inaptitude:
- Périodes d'accumulation de points
- Seuils de suspension de permis
- Impact sur l'assurance
- Processus de retrait des points""",
            "language": "fr",
            "country_id": country_id,
            "keywords": "contravention, excès de vitesse, feu rouge, virage illégal, céder passage, conduite imprudente, course, conduite dangereuse, conduite distraite, sans assurance, permis suspendu, points d'inaptitude, tribunal de la circulation, infraction routière, amende routière, pénalité routière",
            "source": "Code de la route",
            "section": "Infractions routières",
            "year": 2023
        }
    ]
    
    for law_data in french_laws:
        law = Law(**law_data)
        db.session.add(law)

if __name__ == "__main__":
    init_all_laws()
