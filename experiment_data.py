# experiment_data.py

experiment_data = {
    "property": {
        "name": "Charmante Altbauwohnung",
        "location": "Kreuzviertel, Münster",
        "size": "90 m²",
        "rooms": 3,
        "year_built": 1920,
        "market_value": 350000,
        "description": "Diese stilvolle Altbauwohnung bietet hohe Decken, große Fenster und historische Elemente."
    },
    "treatments": [
        {"treatment_name": "Niedriger Ankerpreis", "start_price": 320000},
        {"treatment_name": "Marktpreis", "start_price": 350000},
        {"treatment_name": "Hoher Ankerpreis", "start_price": 380000}
    ],
    "rounds": 1,
    "buyer_profiles": [
        {
            "name": "Familienkäufer",
            "preferences": "Eine geräumige Wohnung mit mehreren Schlafzimmern, in der Nähe von Schulen und Spielplätzen.",
            "age": 35,
            "income": 60000,
            "marital_status": "verheiratet"
        },
        {
            "name": "Investitionskäufer",
            "preferences": "Eine Immobilie mit hohem Renditepotenzial, idealerweise in einer aufstrebenden Nachbarschaft.",
            "age": 40,
            "income": 80000,
            "marital_status": "ledig"
        },
        {
            "name": "Erstkäufer",
            "preferences": "Eine bezahlbare Wohnung in einer sicheren Nachbarschaft, mit guter Anbindung an öffentliche Verkehrsmittel.",
            "age": 28,
            "income": 40000,
            "marital_status": "ledig"
        }
    ]
}
