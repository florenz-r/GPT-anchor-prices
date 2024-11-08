import pandas as pd
import matplotlib.pyplot as plt


data = {
    "Niedriger Ankerpreis": {
        "marktwerte": [680000, 650000, 680000, 690000, 700000, 660000, 680000, 680000, 680000, 650000, 690000, 650000, 680000, 680000, 650000, 680000, 650000, 690000, 670000, 685000, 680000, 680000, 650000, 670000, 650000, 690000, 700000, 650000, 690000, 680000],
        "zahlungsbereitschaft": [650000, 600000, 650000, 650000, 650000, 650000, 650000, 650000, 650000, 620000, 690000, 620000, 650000, 650000, 600000, 650000, 600000, 650000, 650000, 650000, 650000, 650000, 600000, 650000, 600000, 670000, 650000, 600000, 680000, 650000]
    },
    "Marktpreis": {
        "marktwerte": [720000, 720000, 720000, 700000, 720000, 720000, 700000, 710000, 700000, 700000, 700000, 720000, 700000, 700000, 720000, 700000, 700000, 710000, 700000, 700000, 700000, 700000, 700000, 690000, 700000, 720000, 700000, 710000, 700000, 700000],
        "zahlungsbereitschaft": [700000, 700000, 700000, 650000, 700000, 700000, 650000, 680000, 650000, 650000, 650000, 700000, 650000, 650000, 700000, 680000, 650000, 700000, 650000, 650000, 650000, 650000, 650000, 650000, 650000, 700000, 650000, 700000, 650000, 650000]
    },
    "Hoher Ankerpreis": {
        "marktwerte": [750000, 750000, 750000, 740000, 750000, 750000, 725000, 750000, 760000, 750000, 740000, 720000, 750000, 750000, 750000, 750000, 750000, 750000, 740000, 750000, 750000, 750000, 750000, 740000, 720000, 750000, 750000, 740000, 750000, 750000],
        "zahlungsbereitschaft": [700000, 700000, 700000, 725000, 720000, 700000, 700000, 700000, 750000, 700000, 700000, 680000, 700000, 725000, 700000, 700000, 700000, 700000, 710000, 700000, 700000, 700000, 720000, 700000, 700000, 700000, 700000, 700000, 700000, 700000]
    }
}

# Erstelle den DataFrame
df = pd.DataFrame({
    "Behandlung": ["Niedriger Ankerpreis"] * len(data["Niedriger Ankerpreis"]["marktwerte"]) +
                  ["Marktpreis"] * len(data["Marktpreis"]["marktwerte"]) +
                  ["Hoher Ankerpreis"] * len(data["Hoher Ankerpreis"]["marktwerte"]),
    "Marktwert": data["Niedriger Ankerpreis"]["marktwerte"] +
                 data["Marktpreis"]["marktwerte"] +
                 data["Hoher Ankerpreis"]["marktwerte"],
    "Zahlungsbereitschaft": data["Niedriger Ankerpreis"]["zahlungsbereitschaft"] +
                            data["Marktpreis"]["zahlungsbereitschaft"] +
                            data["Hoher Ankerpreis"]["zahlungsbereitschaft"]
})

# Durchschnitt und Varianz berechnen
mean_var = df.groupby("Behandlung").agg({
    "Marktwert": ["mean", "var"],
    "Zahlungsbereitschaft": ["mean", "var"]
})

# Ergebnisse anzeigen
print("Durchschnitt und Varianz der Marktwerte und Zahlungsbereitschaften:")
print(mean_var)

# Plot erstellen
mean_var["Marktwert"]["mean"].plot(kind="bar", color="blue", alpha=0.6, label="Marktwert (Durchschnitt)")
mean_var["Zahlungsbereitschaft"]["mean"].plot(kind="bar", color="orange", alpha=0.6, label="Zahlungsbereitschaft (Durchschnitt)")
plt.title("Durchschnittlicher Marktwert und Zahlungsbereitschaft pro Behandlung")
plt.ylabel("Euro")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
