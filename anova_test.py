import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

# Daten für die ANOVA vorbereiten
data = {
    'Treatment': (
        ['Low Anchor Price'] * 30 +
        ['Market Price'] * 30 +
        ['High Anchor Price'] * 30
    ),
    'Market Value': (
        680000, 650000, 680000, 690000, 700000, 660000, 680000, 680000, 680000, 650000,
        690000, 650000, 680000, 680000, 650000, 680000, 650000, 690000, 670000, 685000,
        680000, 680000, 650000, 670000, 650000, 690000, 700000, 650000, 690000, 680000,
        720000, 720000, 720000, 700000, 720000, 720000, 700000, 710000, 700000, 700000,
        700000, 720000, 700000, 700000, 720000, 700000, 700000, 710000, 700000, 700000,
        700000, 700000, 700000, 690000, 700000, 720000, 700000, 710000, 700000, 700000,
        750000, 750000, 750000, 740000, 750000, 750000, 725000, 750000, 760000, 750000,
        740000, 720000, 750000, 750000, 750000, 750000, 750000, 750000, 740000, 750000,
        750000, 750000, 750000, 740000, 720000, 750000, 750000, 740000, 750000, 750000
    ),
    'Willingness to Pay': (
        650000, 600000, 650000, 650000, 650000, 650000, 650000, 650000, 650000, 620000,
        690000, 620000, 650000, 650000, 600000, 650000, 600000, 650000, 650000, 650000,
        650000, 650000, 600000, 650000, 600000, 670000, 650000, 600000, 680000, 650000,
        700000, 700000, 700000, 650000, 700000, 700000, 650000, 680000, 650000, 650000,
        650000, 700000, 650000, 650000, 700000, 680000, 650000, 700000, 650000, 650000,
        650000, 650000, 650000, 650000, 650000, 700000, 650000, 700000, 650000, 650000,
        700000, 700000, 700000, 725000, 720000, 700000, 700000, 700000, 750000, 700000,
        700000, 680000, 700000, 725000, 700000, 700000, 700000, 700000, 710000, 700000,
        700000, 700000, 720000, 700000, 700000, 700000, 700000, 700000, 700000, 700000
    )
}

# DataFrame erstellen
df = pd.DataFrame(data)

# ANOVA für 'Market Value'
model_market_value = ols('Q("Market Value") ~ C(Treatment)', data=df).fit()
anova_results_market_value = sm.stats.anova_lm(model_market_value, typ=2)

# ANOVA für 'Willingness to Pay'
model_willingness_to_pay = ols('Q("Willingness to Pay") ~ C(Treatment)', data=df).fit()
anova_results_willingness_to_pay = sm.stats.anova_lm(model_willingness_to_pay, typ=2)

# Ergebnisse ausdrucken
print("ANOVA-Ergebnisse für 'Market Value':")
print(anova_results_market_value)
print("\nANOVA-Ergebnisse für 'Willingness to Pay':")
print(anova_results_willingness_to_pay)
