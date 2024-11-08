import json
import random

# Beispiel-Daten für das Experiment
experiment_data = {
    "threads": [
        [1, "GPTThread (GPT-4)"],
        [2, "GPTThread (GPT-4)"]
    ],
    "treatments": [
        "Lowstartprice",
        "Marketstartprice",
        "Highstartprice"
    ],
    "rounds": 10,
    "variables": {
        "start_price": {
            "Lowstartprice": 270000,
            "Marketstartprice": 300000,
            "Highstartprice": 330000
        }
    },
    "prompts": {
        "system": (
            "Du nimmst an einem Entscheidungsfindungsexperiment teil, das zwei Personen umfasst: "
            "Einen Verkäufer und einen Käufer.\n"
            "\n{% if i == 1 %}\n"
            "Du bist der Verkäufer. Das bedeutet, dass du den Startpreis für die Immobilie festlegen wirst.\n"
            "\n{% else %}\n"
            "Du bist der Käufer. Das bedeutet, dass du ein Gebot abgeben wirst, nachdem der Verkäufer den Startpreis festgelegt hat.\n"
            "\n{% endif %}\n"
            "Folge immer den Anweisungen. Entschuldige dich nicht. Gib nur das zurück, was erwartet wird."
        ),
        "user": (
            "{% if i == 1 %}\n"
            "Du bist der Verkäufer. Deine Aufgabe ist es, den Startpreis für eine Immobilie mit einem Marktwert von 300000 Euro festzulegen.\n"
            "\nBitte gib den Startpreis im folgenden Format an:\n"
            "{\"start_price\": /*dein Startpreis*/}\n"
            "Nachdem du den Startpreis festgelegt hast, wird der Käufer darauf reagieren und sein Gebot abgeben.\n"
            "{% elif i == 2 %}\n"
            "Du bist der Käufer. Der Verkäufer hat den Startpreis festgelegt.\n"
            "Die Immobilie hat einen Marktwert von 300000 Euro. Der Verkäufer hat einen Startpreis von {{ other.choices[-1] }} Euro festgelegt.\n"
            "Bitte gib dein maximales Gebot im folgenden Format ab:\n"
            "{\"endpreis\": /*dein Preis*/}\n"
            "{% endif %}\n"
        )
    },
    "filters": [
        ["extract_number"],
        ["extract_number"],
        ["JSON"],
        ["JSON"]
    ]
}

# Funktion für das Experiment
def run_experiment():
    # Simulation für jeden Behandlung
    for treatment in experiment_data["treatments"]:
        start_price = experiment_data["variables"]["start_price"][treatment]
        print(f"Behandlung: {treatment}, Startpreis: {start_price}")

        for round_num in range(1, experiment_data["rounds"] + 1):
            print(f"Runde {round_num}")

            if round_num % 2 != 0:  # Verkäufer
                user_prompt = f"Du bist der Verkäufer. Setze den Startpreis für die Immobilie fest: {start_price} Euro."
                # Simuliere die Entscheidung des Verkäufers
                seller_response = {"start_price": start_price}  # Hier könntest du die Logik erweitern
                print(f"Antwort vom Verkäufer: {json.dumps(seller_response)}")

            else:  # Käufer
                user_prompt = f"Du bist der Käufer. Der Verkäufer hat den Startpreis von {start_price} Euro festgelegt."
                # Simuliere die Entscheidung des Käufers (ein einfaches zufälliges Gebot als Beispiel)
                buyer_offer = random.randint(240000, 290000)  # Beispielangebot
                buyer_response = {"endpreis": buyer_offer}
                print(f"Antwort vom Käufer: {json.dumps(buyer_response)}")

# Experiment starten
if __name__ == "__main__":
    run_experiment()

