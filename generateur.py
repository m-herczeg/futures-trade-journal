import random
import pandas as pd

random.seed(42)

specs = {
    "ES": {"mult": 50, "prix": 5000, "mouvement": 10},
    "NQ": {"mult": 20, "prix": 18000, "mouvement": 40},
    "CL": {"mult": 1000, "prix": 78, "mouvement": 0.5},
    "GC": {"mult": 100, "prix": 2000, "mouvement": 8},
}

def pnl_trade(prix_entree, prix_sortie, quantite, multiplicateur, sens):
    resultat = (prix_sortie - prix_entree) * quantite * multiplicateur * sens
    return resultat

trades = []

for i in range(100):
    contrat = random.choice(["ES", "NQ", "CL", "GC"])
    fiche = specs[contrat]
    sens = random.choice([1, -1])
    quantite = random.randint(1, 3)

    prix_entree = fiche["prix"]
    prix_sortie = round(prix_entree + random.uniform(-fiche["mouvement"], fiche["mouvement"]), 2)
    pnl = pnl_trade(prix_entree, prix_sortie, quantite, fiche["mult"], sens)

    trade = {
        "contrat": contrat,
        "sens": sens,
        "quantite": quantite,
        "prix_entree": prix_entree,
        "prix_sortie": round(prix_sortie, 2),
        "pnl": round(pnl, 2),
    }
    trades.append(trade)

df = pd.DataFrame(trades)
df.to_csv("trades.csv", index=False)
print(df)
print("Fichier trades.csv enregistré")