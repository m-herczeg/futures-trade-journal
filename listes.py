pnls = [1050.0, 500, 500.0, -400, -120]
print(f"Nombre de trade : {len(pnls)}")
print(f"P&L total : {sum(pnls)} $")
print(f"Gain moyen : {sum(pnls)/len(pnls)} $")
print(f"Meilleur trade : {max(pnls)} $")
print(f"Pire trade : {min(pnls)} $")