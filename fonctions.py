def pnl_trade(prix_entree, prix_sortie, quantite, multiplicateur):
    resultat = (prix_sortie - prix_entree) * quantite * multiplicateur
    return resultat

pnl_es = pnl_trade(5000.25, 5010.75, 2, 50)
print(f"P&L ES : {pnl_es} $")

pnl_nq = pnl_trade(18000, 18025, 1, 20)
print(f"P&L NQ : {pnl_nq} $")