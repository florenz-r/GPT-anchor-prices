import openai
import json
import random  # Für zufällige Varianz

from experiment_data import experiment_data  # Importiere die Experimentstruktur

# API-Schlüssel aus einer Datei laden
def load_openai_key():
    with open("openai_key", "r") as file:
        return file.read().strip()

# Käuferprofile mit flexiblerer Budgetgrenze
buyer_profiles = [
    {"name": "Junger Berufstätiger", "budget": 320000, "flexibility": 0.1},  # 10% Flexibilität
    {"name": "Familienkäufer", "budget": 370000, "flexibility": 0.15},  # 15% Flexibilität
    {"name": "Investitionskäufer", "budget": 400000, "flexibility": 0.2},  # 20% Flexibilität
    {"name": "Sparsame Käuferin", "budget": 300000, "flexibility": 0.05}  # 5% Flexibilität
]

# Funktion für GPT-4-Anfrage mit Temperatur
def ask_gpt(system_prompt, user_prompt, temperature=0.7):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=temperature  # Temperatur hinzufügen
    )
    return response['choices'][0]['message']['content'].strip()

# Funktion zur Berechnung der flexiblen Zahlungsbereitschaft
def calculate_max_bid(budget, flexibility):
    variance = random.uniform(-flexibility, flexibility)  # Zufällige Varianz innerhalb der Flexibilität
    return round(budget * (1 + variance))

# Funktion für das Experiment
def run_experiment():
    # API-Schlüssel laden
    api_key = load_openai_key()
    openai.api_key = api_key

    # System-Prompt für den Käufer
    system_prompt = (
        "Du nimmst an einem Entscheidungsfindungsexperiment teil. "
        "Gib nur einen numerischen Wert für deine maximale Zahlungsbereitschaft an, "
        "basierend auf dem Startpreis und dem Marktwert. "
        "Gib keine Erklärungen oder zusätzlichen Text zurück."
    )

    # Öffne eine Datei zum Speichern der Antworten
    with open('chatgpt_responses6', 'w') as file:
        # Marktwert der Immobilie
        market_value = 350000
        file.write(f"Marktwert der Immobilie: {market_value} Euro\n")

        # Iteriere über die verschiedenen Ankerpreise und Käuferprofile
        for treatment in experiment_data["treatments"]:
            start_price = treatment["start_price"]
            treatment_name = treatment["treatment_name"]
            print(f"Behandlung: {treatment_name}, Startpreis: {start_price}")
            file.write(f"Behandlung: {treatment_name}, Startpreis: {start_price}\n")

            for profile in buyer_profiles:
                print(f"Käuferprofil: {profile['name']}")
                file.write(f"Käuferprofil: {profile['name']}\n")

                for round_num in range(1, experiment_data["rounds"] + 1):
                    print(f"Runde {round_num}")
                    file.write(f"Runde {round_num}\n")

                    # Berechne die flexible Zahlungsbereitschaft mit Varianz
                    max_bid = calculate_max_bid(profile['budget'], profile['flexibility'])

                    # Prompt, der den Startpreis im Vergleich zum Marktwert klarstellt
                    user_prompt = (
                        f"Der Verkäufer hat einen Startpreis von {start_price} Euro für die Immobilie '{experiment_data['property']['name']}' "
                        f"angegeben. Der Marktwert der Immobilie beträgt {market_value} Euro. "
                        f"Dein Budget liegt bei {profile['budget']} Euro, aber du kannst flexibel bis zu {profile['flexibility']*100}% "
                        f"über oder unter deinem Budget bieten. "
                        "Was ist deine maximale Zahlungsbereitschaft? Gib nur eine Zahl ohne Erklärungen an."
                    )

                    buyer_response = ask_gpt(system_prompt, user_prompt)
                    print(f"Antwort vom Käufer: {buyer_response} (flexible max: {max_bid})")
                    file.write(f"Antwort vom Käufer: {buyer_response} (flexible max: {max_bid})\n")


# Experiment starten
if __name__ == "__main__":
    run_experiment()
