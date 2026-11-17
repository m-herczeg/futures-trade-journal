pnls = [1050.0, 500, 500.0, -400, -120]

for pnl in pnls:
        if pnl < -300:
              print(f"Alerte : {pnl} $ dépasse la limite")
        else:
            print(f"Ok : {pnl} $")