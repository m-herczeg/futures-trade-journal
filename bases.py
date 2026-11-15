contrat = "ES"
quantite = 2 
prix_entree = 5000.25
prix_sortie = 5010.75
multiplicateur = 50

pnl = (prix_sortie - prix_entree) * quantite * multiplicateur

frais_par_contrat = 2.50
frais = (frais_par_contrat * quantite) * 2
pnl_net = (pnl - frais)
print(f"P&L brut sur {contrat} : {pnl} $")
print(f"frais sur {contrat} : {frais} $")
print(f"P&L net sur {contrat} : {pnl_net} $")