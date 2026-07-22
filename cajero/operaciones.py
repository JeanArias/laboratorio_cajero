"""
operaciones.py

Contiene las funciones relacionadas con las operaciones
del cajero automático.
"""

SALDO_INICIAL = 1000000

def retirar_dinero(saldo, monto):
    """
    Realiza el retiro de dinero validando las reglas del negocio.

    Parámetros:
        saldo (float): Saldo disponible.
        monto (float): Monto solicitado.

    Retorna:
        float: Nuevo saldo.
    """

    if monto < 0:
        raise ValueError("El monto no puede ser negativo.")

    if monto > saldo:
        raise ValueError("Fondos insuficientes.")

    return saldo - monto