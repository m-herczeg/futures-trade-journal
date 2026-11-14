import pandas as pd

trades = pd.DataFrame({
    "contrat": ["ES", "NQ", "CL"],
    "pnl": [250.0, -120.0, 480.0],
})
print(trades)
print("P&L total :", trades["pnl"].sum())
