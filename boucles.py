pnls = [1050.0, 500, 500.0, -400, -120]

nb_alertes = 0

for pnl in pnls:
        if pnl < -300:
              print(f"Alerte : {pnl} $ dépasse la limite")
              nb_alertes = nb_alertes + 1 
        else:
            print(f"Ok : {pnl} $")

print(f"Nombre d'alertes : {nb_alertes}")
