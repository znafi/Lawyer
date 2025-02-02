from app import app, db, Country, Law

def init_database():
    with app.app_context():
        # Create tables
        db.create_all()

        # Check if we already have data
        if Country.query.first() is None:
            # Add some sample countries
            countries = [
                {"name": "United States", "code": "US"},
                {"name": "United Kingdom", "code": "GB"},
                {"name": "Canada", "code": "CA"},
                {"name": "Australia", "code": "AU"},
                {"name": "India", "code": "IN"},
                {"name": "Germany", "code": "DE"},
                {"name": "France", "code": "FR"},
                {"name": "Japan", "code": "JP"},
                {"name": "Brazil", "code": "BR"},
                {"name": "China", "code": "CN"}
            ]

            # Add countries to database
            for country_data in countries:
                country = Country(name=country_data["name"], code=country_data["code"])
                db.session.add(country)
            
            # Sample law for US (First Amendment)
            us_country = Country.query.filter_by(code="US").first()
            first_amendment = Law(
                title="First Amendment",
                content="Congress shall make no law respecting an establishment of religion, or prohibiting the free exercise thereof; or abridging the freedom of speech, or of the press; or the right of the people peaceably to assemble, and to petition the Government for a redress of grievances.",
                language="en",
                country_id=us_country.id,
                keywords="freedom of speech, religion, press, assembly, petition",
                source="United States Constitution, Bill of Rights",
                section="Amendment I",
                year=1791
            )
            db.session.add(first_amendment)

            # Commit the changes
            db.session.commit()
            print("Database initialized with sample data!")

if __name__ == "__main__":
    init_database()
