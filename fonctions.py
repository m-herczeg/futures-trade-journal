def pnl_trade(prix_entree, prix_sortie, quantite, multiplicateur, sens):
    resultat = (prix_sortie - prix_entree) * quantite * multiplicateur * sens
    return resultat

pnl_es = pnl_trade(5000.25, 5010.75, 2, 50, 1)
print(f"P&L ES : {pnl_es} $")

pnl_nq = pnl_trade(18000, 18025, 1, 20, 1)
print(f"P&L NQ : {pnl_nq} $")

pnl_cl = pnl_trade(78.40, 77.90, 1, 1000, -1)
print(f"P&L CL : {pnl_cl} $")