trades = [
    {"contrat": "ES", "sens": "long", "quantite": 2, "pnl": 1050.0},
    {"contrat": "NQ", "sens": "long", "quantite": 1, "pnl": 500},
    {"contrat": "CL", "sens": "short", "quantite": 1, "pnl": 500.0},
    {"contrat": "ES", "sens": "long", "quantite": 1, "pnl": -400},
    {"contrat": "GC", "sens": "short", "quantite": 1, "pnl": -120},
]

nb_alertes = 0

for trade in trades:
    if trade["pnl"] < -300:
        print(f"Alerte : {trade['contrat']} {trade['sens']}, {trade['pnl']} $, depasse la limite")
        nb_alertes = nb_alertes + 1
    else:
        print(f"Ok : {trade['contrat']} {trade['sens']}, {trade['pnl']} $")

print(f"Nombre d'alertes : {nb_alertes}")