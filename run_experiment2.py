import openai
import json


# API-Schlüssel aus einer Datei laden
def load_openai_key():
    with open("openai_key", "r") as file:
        return file.read().strip()


# Funktion für GPT-4-Anfrage
def ask_gpt(system_prompt, user_prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )
    return response['choices'][0]['message']['content'].strip()


# Funktion für das Experiment
def run_experiment():
    # API-Schlüssel laden
    api_key = load_openai_key()
    openai.api_key = api_key

    # Experiment-Daten basierend auf deiner JSON-Definition
    experiment_data = {
        "threads": [
            [1, "GPTThread (GPT-4)"],
            [2, "GPTThread (GPT-4)"]
        ],
        "treatments": ["Lowstartprice", "Marketstartprice", "Highstartprice"],
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
                "Bitte gib deine maximale Zahlungsbereitschaft im folgenden Format ab:\n"
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

    # Öffne eine Datei zum Speichern der Antworten
    with open('chatgpt_responses.5', 'w') as file:
        # Simulation für jede Behandlung
        for treatment in experiment_data["treatments"]:
            start_price = experiment_data["variables"]["start_price"][treatment]
            print(f"Behandlung: {treatment}, Startpreis: {start_price}")
            file.write(f"Behandlung: {treatment}, Startpreis: {start_price}\n")

            for round_num in range(1, experiment_data["rounds"] + 1):
                print(f"Runde {round_num}")
                file.write(f"Runde {round_num}\n")

                # User-Prompt für Verkäufer und Käufer
                if round_num % 2 != 0:  # Verkäufer
                    user_prompt = f"Setze den Startpreis für die Immobilie fest: {start_price} Euro."
                    seller_response = ask_gpt(experiment_data["prompts"]["system"], user_prompt)
                    print(f"Antwort vom Verkäufer: {seller_response}")
                    file.write(f"Antwort vom Verkäufer: {seller_response}\n")
                else:  # Käufer
                    user_prompt = (
                        f"Der Verkäufer hat den Startpreis von {start_price} Euro festgelegt. "
                        "Bitte gib deine maximale Zahlungsbereitschaft für diese Immobilie an."
                    )
                    buyer_response = ask_gpt(experiment_data["prompts"]["system"], user_prompt)
                    print(f"Antwort vom Käufer: {buyer_response}")
                    file.write(f"Antwort vom Käufer: {buyer_response}\n")


# Experiment starten
if __name__ == "__main__":
    run_experiment()
