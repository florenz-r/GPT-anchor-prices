import openai
import json
from experiment_data import experiment_data  # Importiere die Experimentstruktur


# API-Schlüssel aus einer Datei laden
def load_openai_key():
    with open("openai_key", "r") as file:
        return file.read().strip()


# Funktion für GPT-4-Anfrage
def ask_gpt(system_prompt, user_prompt,):
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

    # System-Prompt für den Käufer
    system_prompt = (
        "Du nimmst an einem Entscheidungsfindungsexperiment teil. "
        "Gib nur einen numerischen Wert für deine maximale Zahlungsbereitschaft an, "
        "basierend auf dem Startpreis und dem Marktwert. "
        "Gib keine Erklärungen oder zusätzlichen Text zurück."
    )

    # Öffne eine Datei zum Speichern der Antworten
    with open('chatgpt_responses01', 'w') as file:
        # Iteriere über die verschiedenen Ankerpreise
        for treatment in experiment_data["treatments"]:
            start_price = treatment["start_price"]
            treatment_name = treatment["treatment_name"]
            print(f"Behandlung: {treatment_name}, Startpreis: {start_price}")
            file.write(f"Behandlung: {treatment_name}, Startpreis: {start_price}\n")

            for round_num in range(1, experiment_data["rounds"] + 1):
                print(f"Runde {round_num}")
                file.write(f"Runde {round_num}\n")

                user_prompt = (
                    f"Der Verkäufer hat einen Startpreis von {start_price} Euro für die Immobilie '{experiment_data['property']['name']}' "
                    f"angegeben. Was ist deine maximale Zahlungsbereitschaft für diese Immobilie? "
                    "Gib nur eine Zahl ohne Erklärungen an."
                )

                buyer_response = ask_gpt(system_prompt, user_prompt)
                print(f"Antwort vom Käufer: {buyer_response}")
                file.write(f"Antwort vom Käufer: {buyer_response}\n")


# Experiment starten
if __name__ == "__main__":
    run_experiment()