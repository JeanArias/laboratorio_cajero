class FondosInsuficientesError(Exception):
    """Excepción para cuando el monto a retirar supera el saldo disponible."""
    pass

class MontoMinimoError(Exception):
    """Excepción para cuando el monto es menor al mínimo permitido ($10)."""
    pass

def retirar_dinero(saldo, monto):
    if monto < 10:
        raise MontoMinimoError("El monto mínimo de retiro es de $10.")
    
    if monto > saldo:
        raise FondosInsuficientesError("No tienes fondos suficientes para realizar este retiro.")
    
    return saldo - monto