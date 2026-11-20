import pandas as pd

trades = [
    {"contrat": "ES", "sens": "long", "quantite": 2, "pnl": 1050.0},
    {"contrat": "NQ", "sens": "long", "quantite": 1, "pnl": 500},
    {"contrat": "CL", "sens": "short", "quantite": 1, "pnl": 500.0},
    {"contrat": "ES", "sens": "long", "quantite": 1, "pnl": -400},
    {"contrat": "GC", "sens": "short", "quantite": 1, "pnl": -120},
]

df = pd.DataFrame(trades)
alertes = df[df["pnl"] < -300]
df["frais"] = df["quantite"] * 2.50 * 2
df["pnl_net"] = df["pnl"] - df["frais"]
print(df)

print(f"Nombre de trades : {len(df)}")
print(f"P&L total : {df['pnl'].sum()} $")
print(f"P&L moyen : {df["pnl"].mean()} $")
print(f"Meilleur trade : {df["pnl"].max()} $")
print(f"Pire trade : {df["pnl"].min()} $")
print(alertes)
print(f"Nombre d'alertes : {len(alertes)}")
