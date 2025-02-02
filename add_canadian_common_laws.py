from app import app, db, Country, Law

def add_canadian_common_laws():
    with app.app_context():
        canada = Country.query.filter_by(code="CA").first()
        if not canada:
            print("Error: Canada not found in database")
            return

        common_laws = [
            {
                "title": "Speed Limits and Speeding Penalties",
                "content": """Speed Limits in Canada:
- School zones: 30-50 km/h
- Urban areas: 40-50 km/h
- Rural roads: 80 km/h
- Highways: 100-110 km/h

Penalties for Speeding:
- 1-20 km/h over: $100-$200 fine
- 21-30 km/h over: $225-$295 fine
- 31-50 km/h over: $325-$475 fine + possible license suspension
- 50+ km/h over: $500+ fine, mandatory court appearance, possible criminal charges

Demerit Points:
- 3 points: Exceeding speed limit by 21-30 km/h
- 4 points: Exceeding speed limit by 31-50 km/h
- 6 points: Exceeding speed limit by 50+ km/h""",
                "keywords": "speed limit, speeding, traffic violation, demerit points, driving penalties",
                "source": "Highway Traffic Act",
                "section": "Section 128",
                "year": 2019  # Latest major update to speeding penalties
            },
            {
                "title": "Distracted Driving Laws",
                "content": """Prohibited Activities While Driving:
- Using hand-held communication/entertainment devices
- Viewing display screens unrelated to driving
- Programming GPS devices (except by voice)
- Reading printed materials
- Writing, printing, or sketching

Penalties:
First conviction:
- $615-$1,000 fine
- 3 demerit points
- 3-day license suspension

Subsequent convictions:
- Up to $3,000 fine
- 6 demerit points
- 7-day license suspension

Exceptions:
- Hands-free devices
- Single-touch activation
- Emergency calls to 911
- Viewing GPS display""",
                "keywords": "distracted driving, cell phone, texting, driving penalties",
                "source": "Highway Traffic Act",
                "section": "Section 78.1",
                "year": 2022  # Latest update to distracted driving penalties
            },
            {
                "title": "Right-of-Way Rules",
                "content": """Right-of-Way Regulations:

1. Intersections:
- Yield to vehicles already in intersection
- Yield to right when arriving simultaneously
- Left turn yields to oncoming traffic
- Emergency vehicles have priority

2. Pedestrians:
- Always yield to pedestrians at crosswalks
- Yield to pedestrians at intersections
- Stop for school crossing guards
- Extra caution in school zones

3. Special Circumstances:
- Yield to emergency vehicles
- Yield to public transit buses
- Yield to funeral processions
- Yield at merge points

4. Roundabouts:
- Yield to vehicles already in roundabout
- Signal when exiting
- Stay in lane until exit
- Watch for pedestrians""",
                "keywords": "right of way, intersection rules, pedestrian rights, traffic rules",
                "source": "Highway Traffic Act",
                "section": "Section 135-141",
                "year": 2015  # Major update to intersection and pedestrian rules
            },
            {
                "title": "Rights During Police Interactions",
                "content": """Your Rights When Interacting with Police:

1. Right to Know Why You're Being Stopped:
- Police must inform you of the reason for any detention or arrest
- You have the right to be informed promptly of the reason

2. Right to Remain Silent:
- You have the right to remain silent
- You only need to identify yourself if:
  * You're under arrest
  * You're driving (must show license, registration, insurance)
  * You're suspected of a crime

3. Right to Legal Counsel:
- You have the right to speak to a lawyer
- Police must stop questioning once you request a lawyer
- You have the right to free legal advice through Legal Aid

4. Search Rights:
- Police need a warrant to search your home
- Exception: Emergency circumstances or consent
- Police can pat you down for weapons if they have reasonable grounds
- During traffic stops, police can search your vehicle if they have reasonable grounds

5. Recording Rights:
- You can record police interactions in public places
- Cannot interfere with police duties while recording""",
                "keywords": "police rights, arrest rights, legal counsel, search and seizure, police interaction",
                "source": "Canadian Charter of Rights and Freedoms, Criminal Code",
                "section": "Sections 7-14, Charter",
                "year": 2023
            },
            {
                "title": "Self-Defense Rights",
                "content": """Legal Self-Defense in Canada:

1. When Self-Defense is Legal:
- Reasonable belief that force is being used against you
- Response must be proportional to the threat
- Must be acting in defense of yourself or others

2. Reasonable Force:
- Only as much force as necessary to stop the threat
- Force must stop when the threat ends
- Excessive force may result in criminal charges

3. Castle Doctrine (Home Defense):
- Right to defend your home from intruders
- Must still use reasonable force
- No duty to retreat from your own home

4. What is NOT Self-Defense:
- Revenge or retaliation
- Starting a fight then claiming self-defense
- Using force after the threat has passed
- Excessive force beyond what's necessary

5. Legal Consequences:
- Must report self-defense incidents to police
- May need to justify your actions in court
- Keep detailed records of what happened""",
                "keywords": "self defense, reasonable force, castle doctrine, physical altercation, fighting",
                "source": "Criminal Code of Canada",
                "section": "Section 34",
                "year": 2023
            },
            {
                "title": "Assault and Battery Laws",
                "content": """Types of Assault in Canada:

1. Simple Assault (Level 1):
- Applying force without consent
- Attempting or threatening to apply force
- Penalties: Up to 5 years imprisonment

2. Assault with Weapon (Level 2):
- Using or threatening to use a weapon
- Causing bodily harm
- Penalties: Up to 10 years imprisonment

3. Aggravated Assault (Level 3):
- Wounding, maiming, disfiguring
- Endangering life
- Penalties: Up to 14 years imprisonment

4. Sexual Assault:
- Sexual contact without consent
- Varying degrees of severity
- Penalties: Up to life imprisonment

5. Domestic Assault:
- Assault against family members
- Special provisions for protection
- May include restraining orders

Defenses:
- Self-defense
- Defense of others
- Consent (in specific circumstances)
- Accident or lack of intent""",
                "keywords": "assault, battery, fighting, violence, criminal charges, domestic violence",
                "source": "Criminal Code of Canada",
                "section": "Sections 265-268",
                "year": 2023
            },
            {
                "title": "Property Dispute Laws",
                "content": """Common Property Disputes and Legal Rights:

1. Neighbor Disputes:
- Property boundaries
- Noise complaints (bylaws vary by municipality)
- Tree and fence issues
- Property damage

Resolution Process:
a) Talk to neighbor first
b) Document everything
c) Contact municipal bylaw office
d) Mediation services
e) Small claims court (up to $35,000)

2. Landlord-Tenant Disputes:
- Rent payments
- Maintenance and repairs
- Eviction notices
- Security deposits

Resolution Process:
a) Written notice to other party
b) Document all communication
c) Contact Landlord and Tenant Board
d) File formal complaint

3. Trespassing:
- Entry without permission
- Remaining after being asked to leave
- Penalties: Fines up to $10,000

4. Noise Complaints:
- Quiet hours (typically 11 PM - 7 AM)
- Construction noise restrictions
- Excessive noise fines
- Process: Contact bylaw enforcement""",
                "keywords": "property dispute, neighbor dispute, landlord, tenant, trespassing, noise complaint",
                "source": "Provincial Property Acts, Municipal Bylaws",
                "section": "Various",
                "year": 2023
            }
        ]

        # Add laws to database
        for law in common_laws:
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
        print("Canadian common laws successfully added to database!")

if __name__ == "__main__":
    add_canadian_common_laws()
