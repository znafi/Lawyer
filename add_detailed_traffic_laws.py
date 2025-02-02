from app import app, db, Country, Law

def add_detailed_traffic_laws():
    with app.app_context():
        canada = Country.query.filter_by(code="CA").first()
        if not canada:
            print("Error: Canada not found in database")
            return

        traffic_laws = [
            {
                "title": "Traffic Stop Procedures and Rights",
                "content": """What to Do During a Traffic Stop:

1. Initial Stop:
- Pull over safely to the right side
- Stay in your vehicle unless instructed otherwise
- Keep hands visible on steering wheel
- Turn on interior light if dark

2. Required Documents:
- Driver's license
- Vehicle registration
- Insurance documentation
- Keep documents easily accessible

3. Your Rights During Traffic Stops:
- Right to remain silent beyond identifying yourself
- Right to record the interaction
- Right to refuse vehicle search (unless police have probable cause)
- Right to know why you were stopped

4. Police Powers During Traffic Stop:
- Can request license and registration
- Can inspect vehicle's safety equipment
- Can conduct sobriety tests if impairment suspected
- Can issue tickets or warnings""",
                "keywords": "traffic stop, police stop, vehicle stop, pull over, traffic rights, police interaction, vehicle documents",
                "source": "Highway Traffic Act, Canadian Charter of Rights and Freedoms",
                "section": "Section 33, Section 48",
                "year": 1990  # Major amendments to Highway Traffic Act regarding police powers
            },
            {
                "title": "Vehicle Documentation Requirements",
                "content": """Required Vehicle Documentation:

1. Driver's License:
- Must be valid for vehicle class
- Must be carried while driving
- Must be from province of residence
- International licenses valid for 90 days

2. Vehicle Registration:
- Must be current and valid
- Must match vehicle details
- Must be carried in vehicle
- Must be produced upon request

3. Insurance Documentation:
- Minimum $200,000 liability coverage
- Must be valid and current
- Must be carried in vehicle
- Must be produced upon request

4. Safety Standards Certificate:
- Required for vehicle transfer
- Valid for 36 days
- Must meet provincial standards
- Must be issued by licensed mechanic""",
                "keywords": "driver's license, vehicle registration, insurance, documentation, safety certificate",
                "source": "Highway Traffic Act, Insurance Act",
                "section": "Section 7, Section 32",
                "year": 1994  # Major update to documentation requirements
            },
            {
                "title": "DUI and Sobriety Testing Procedures",
                "content": """Impaired Driving Laws and Procedures:

1. Blood Alcohol Concentration (BAC) Limits:
- 0.08% - Criminal Code offense
- 0.05-0.079% - Provincial sanctions
- Zero tolerance for new drivers

2. Mandatory Alcohol Screening:
- Police can demand breath sample
- No reasonable suspicion required
- Refusal is a criminal offense

3. Testing Procedures:
- Roadside screening device
- Evidentiary breath testing
- Blood testing if necessary
- Drug recognition evaluation

4. Penalties:
- First offense: $1000+ fine
- Mandatory driving prohibition
- Criminal record
- Ignition interlock requirement""",
                "keywords": "DUI, impaired driving, alcohol, breathalyzer, blood alcohol, sobriety test",
                "source": "Criminal Code of Canada, Highway Traffic Act",
                "section": "Section 253, Section 254",
                "year": 2018  # Major impaired driving law reform
            },
            {
                "title": "Vehicle Equipment and Safety Requirements",
                "content": """Mandatory Vehicle Equipment:

1. Lighting Requirements:
- Functioning headlights
- Brake lights
- Turn signals
- Emergency flashers

2. Safety Equipment:
- Functional seat belts
- Airbag systems
- Windshield wipers
- Defrosting system

3. Brake Systems:
- Dual brake system
- Emergency brake
- ABS for newer vehicles
- Regular maintenance

4. Other Requirements:
- Proper tire tread depth
- Functional horn
- Unobstructed windows
- Working speedometer""",
                "keywords": "vehicle equipment, safety requirements, lights, brakes, tires, maintenance",
                "source": "Motor Vehicle Safety Act, Highway Traffic Act",
                "section": "Various",
                "year": 2020  # Latest vehicle safety standards update
            }
        ]

        # Add laws to database
        for law in traffic_laws:
            new_law = Law(
                title=law["title"],
                content=law["content"],
                language="en",
                country_id=canada.id,
                keywords=law["keywords"],
                source=law["source"],
                section=law["section"],
                year=law["year"]
            )
            db.session.add(new_law)
        
        db.session.commit()
        print("Detailed traffic laws successfully added to database!")

if __name__ == "__main__":
    add_detailed_traffic_laws()
