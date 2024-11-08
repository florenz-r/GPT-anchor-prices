# experiment_data.py

experiment_data = {
    "property": {
        "name": "Stilvolle Altbauwohnung",
        "location": "Kreuzviertel, Münster",
        "size": "120 m²",
        "rooms": 4,
        "year_built": 1910,
        "market_value": 680000,
        "description": (
            "Diese helle und stilvolle Altbauwohnung im Kreuzviertel von Münster "
            "bietet hohe Decken, große Fenster, originalen Stuck und Fischgrätenparkett. "
            "Die 4-Zimmer-Wohnung umfasst 3 Schlafzimmer, ein großes Wohnzimmer sowie "
            "ein renoviertes Badezimmer und eine moderne Küche mit Einbaugeräten. "
            "Die Wohnung hat einen Balkon mit Blick auf den begrünten Innenhof. "
            "Das Gebäude wurde 2015 umfassend saniert, inklusive moderner Elektrik, "
            "neuer Fenster und einem aktualisierten Heizsystem. Die Umgebung zeichnet sich "
            "durch ihre Nähe zur Innenstadt, dem Aasee und den zahlreichen Cafés, Schulen "
            "und Geschäften aus."
        )
    },
    "treatments": [
        {"treatment_name": "Niedriger Ankerpreis", "start_price": 640000},
        {"treatment_name": "Marktpreis", "start_price": 680000},
        {"treatment_name": "Hoher Ankerpreis", "start_price": 720000}
    ],
    "rounds": 30  # Anzahl der Runden für das Experiment
}
