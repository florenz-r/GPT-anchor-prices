import openai
import time
from experiment_data2 import experiment_data  # Importiere die neuen Daten

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
        ],
        temperature=1  # Temperatur auf 1 setzen
    )
    return response['choices'][0]['message']['content'].strip()

# Funktion für das Experiment
def run_experiment():
    # API-Schlüssel laden
    api_key = load_openai_key()
    openai.api_key = api_key

    # System-Prompt für den Teilnehmer
    system_prompt = (
        "Du nimmst an einem Experiment teil, bei dem du eine Immobilie bewerten sollst. "
        "Antworte nur mit einer Zahl und ohne zusätzliche Erklärungen."
    )

    # Iteriere über die verschiedenen Ankerpreise (Behandlungen)
    for treatment in experiment_data["treatments"]:
        start_price = treatment["start_price"]
        treatment_name = treatment["treatment_name"]
        print(f"Behandlung: {treatment_name}, Startpreis: {start_price}")

        for round_num in range(1, experiment_data["rounds"] + 1):
            print(f"Runde {round_num}")

            # User-Prompt basierend auf den Immobiliendaten
            property_info = experiment_data["property"]
            user_prompt_market_value = (
                f"Der Verkäufer hat einen Startpreis von {start_price} Euro für die Immobilie '{property_info['name']}' "
                f"angegeben. Die Immobilie befindet sich in {property_info['location']}, ist {property_info['size']} groß "
                f"und wurde im Jahr {property_info['year_built']} gebaut. "
                f"Die Beschreibung der Immobilie: {property_info['description']} "
                f"Was denkst du, ist der realistische Marktwert dieser Immobilie?"
            )

            # Frage GPT-4 nach der Schätzung des Marktwerts
            estimated_market_value = ask_gpt(system_prompt, user_prompt_market_value)
            print(f"Geschätzter Marktwert: {estimated_market_value}")

            # Wartezeit einfügen, um das Rate Limit zu vermeiden
            time.sleep(1)

            # User-Prompt zur Zahlungsbereitschaft
            user_prompt_payment = (
                f"Jetzt, nachdem du den Marktwert geschätzt hast, der bei {estimated_market_value} Euro liegt: "
    f"Wie viel wärst du bereit, für diese Immobilie zu zahlen? "
    f"Bitte denke daran, dass deine Antwort realistisch sein sollte, "
    f"basierend auf dem geschätzten Wert. Antworte nur mit einer Zahl."
            )

            # Frage GPT-4 nach der Zahlungsbereitschaft
            willingness_to_pay = ask_gpt(system_prompt, user_prompt_payment)
            print(f"Zahlungsbereitschaft: {willingness_to_pay}")

# Wartezeit einfügen, um das Rate Limit zu vermeiden
            time.sleep(1)

# Experiment starten
if __name__ == "__main__":
    run_experiment()
