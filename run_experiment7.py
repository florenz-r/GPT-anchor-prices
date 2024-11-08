import openai
from experiment_data import experiment_data  # Importiere die Daten

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

    # System-Prompt für den Käufer
    system_prompt = (
        "Du nimmst an einem Entscheidungsfindungsexperiment teil. "
        "Gib nur einen numerischen Wert für dein maximales Gebot ab. "
        "Gib keine Erklärungen oder zusätzlichen Text zurück."
    )

    # Iteriere über die verschiedenen Ankerpreise (Behandlungen)
    for treatment in experiment_data["treatments"]:
        start_price = treatment["start_price"]
        treatment_name = treatment["treatment_name"]
        print(f"Behandlung: {treatment_name}, Startpreis: {start_price}")

        for round_num in range(1, experiment_data["rounds"] + 1):
            print(f"Runde {round_num}")

            # Simuliere mehrere Käufer pro Profil
            for _ in range(1):  # Erhöhe die Stichprobengröße auf 10 pro Käuferprofil
                for profile in experiment_data["buyer_profiles"]:
                    buyer_name = profile["name"]
                    buyer_preferences = profile["preferences"]

                    # User-Prompt basierend auf den Immobiliendaten
                    user_prompt = (
                        f"Der Verkäufer hat einen Startpreis von {start_price} Euro für die Immobilie '{experiment_data['property']['name']}' "
                        f"angegeben. Die Immobilie befindet sich in {experiment_data['property']['location']}, ist {experiment_data['property']['size']} groß "
                        f"und wurde im Jahr {experiment_data['property']['year_built']} gebaut. "
                        f"Du bist ein {buyer_name} und suchst eine Immobilie, die {buyer_preferences}. "
                        f"Was ist dein maximales Gebot? Gib nur eine Zahl ohne Erklärungen an."
                    )

                    # Frage GPT-4 nach der Antwort des Käufers
                    buyer_response = ask_gpt(system_prompt, user_prompt)
                    print(f"Antwort vom {buyer_name}: {buyer_response}")

# Experiment starten
if __name__ == "__main__":
    run_experiment()
