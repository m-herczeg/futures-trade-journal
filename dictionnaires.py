trade = {"contrat": "CL", "sens": "short", "quantite": 1, "pnl": 500.0}

print(f"Trade {trade['contrat']} {trade['sens']}, {trade['quantite']} contrat : {trade['pnl']} $")

print(trade["pnl"] * 2)