from app import app, db, Country, Law

def add_canadian_constitution():
    with app.app_context():
        # Get Canada from the database
        canada = Country.query.filter_by(code="CA").first()
        if not canada:
            print("Error: Canada not found in database")
            return

        # Canadian Constitution Act, 1982 (including the Charter of Rights and Freedoms)
        constitution_parts = [
            {
                "title": "Canadian Charter of Rights and Freedoms",
                "content": """The Canadian Charter of Rights and Freedoms guarantees the rights and freedoms set out in it subject only to such reasonable limits prescribed by law as can be demonstrably justified in a free and democratic society.

Fundamental Freedoms:
Everyone has the following fundamental freedoms:
(a) freedom of conscience and religion;
(b) freedom of thought, belief, opinion and expression, including freedom of the press and other media of communication;
(c) freedom of peaceful assembly; and
(d) freedom of association.

Democratic Rights:
Every citizen of Canada has the right to vote in an election of members of the House of Commons or of a legislative assembly and to be qualified for membership therein.

Mobility Rights:
Every citizen of Canada has the right to enter, remain in and leave Canada.

Legal Rights:
Everyone has the right to life, liberty and security of the person and the right not to be deprived thereof except in accordance with the principles of fundamental justice.

Equality Rights:
Every individual is equal before and under the law and has the right to the equal protection and equal benefit of the law without discrimination.""",
                "keywords": "charter, rights, freedoms, fundamental freedoms, democratic rights, mobility rights, legal rights, equality",
                "source": "Constitution Act, 1982",
                "section": "Part I",
                "year": 1982  # Original enactment of the Charter
            },
            {
                "title": "Distribution of Powers",
                "content": """The Constitution Act, 1867 (originally the British North America Act) sets out the distribution of powers between the federal and provincial governments.

Federal Powers include:
- National Defense
- Criminal Law
- Banking and Currency
- International Trade
- Immigration
- Indigenous Peoples and Lands
- Postal Service
- Census and Statistics
- Navigation and Shipping
- Patents and Copyright
- Marriage and Divorce

Provincial Powers include:
- Education
- Healthcare
- Property and Civil Rights
- Administration of Justice
- Natural Resources
- Municipalities
- Local Works
- Direct Taxation
- Civil and Property Rights""",
                "keywords": "constitution, federal powers, provincial powers, division of powers, jurisdiction",
                "source": "Constitution Act, 1867",
                "section": "Sections 91-92",
                "year": 1867  # Original British North America Act
            }
        ]

        # Add each part of the constitution
        for part in constitution_parts:
            law = Law(
                title=part["title"],
                content=part["content"],
                language="en",
                country_id=canada.id,
                keywords=part["keywords"],
                source=part["source"],
                section=part["section"],
                year=part["year"]
            )
            db.session.add(law)
        
        # Commit the changes
        db.session.commit()
        print("Canadian Constitution successfully added to database!")

if __name__ == "__main__":
    add_canadian_constitution()
