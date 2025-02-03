from app import db, Law

def add_detailed_traffic_laws(country_id):
    traffic_laws = [
        {
            "title": "Traffic Laws and Regulations",
            "content": """General Traffic Laws in Canada:

1. Speed Limits:
- Urban areas: 30-50 km/h
- Highways: 80-100 km/h
- School zones: 30 km/h
- Construction zones: Variable

2. Right of Way Rules:
- Yield to emergency vehicles
- Pedestrian right of way
- Intersection rules
- Merging regulations

3. Traffic Signals:
- Red light rules
- Yellow light rules
- Green light rules
- Turn signals
- Pedestrian signals

4. Road Signs:
- Stop signs
- Yield signs
- Speed limit signs
- Warning signs
- Information signs

5. Parking Rules:
- No parking zones
- Time-limited parking
- Handicap parking
- Fire hydrant clearance
- Snow route parking bans""",
            "language": "en",
            "country_id": country_id,
            "keywords": "traffic law, speed limit, right of way, traffic signal, road sign, parking, traffic rules, driving rules, traffic violation, traffic ticket, speeding, red light, stop sign, yield sign, pedestrian crossing, school zone, construction zone, highway rules, urban driving, road safety, traffic regulation, traffic enforcement, traffic fine, traffic penalty, traffic infraction, traffic offense, driving law, road law, vehicle law, transportation law",
            "source": "Highway Traffic Act",
            "section": "General Traffic Laws",
            "year": 2023
        }
    ]
    
    for law_data in traffic_laws:
        law = Law(**law_data)
        db.session.add(law)
    db.session.commit()

if __name__ == "__main__":
    add_detailed_traffic_laws(1)
