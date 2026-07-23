"""

Contiene la lógica de negocio del Cajero Automático.

"""

SALDO_INICIAL = 250000.00


def convertir_a_colones(monto, tipo_cambio):
    """
    Convierte un monto a colones.

    Parámetros:
        monto (float)
        tipo_cambio (float)

    Retorna:
        float
    """

    return monto * tipo_cambio


def validar_monto(monto):
    """
    Valida que el monto sea mayor que cero.

    Parámetros:
        monto (float)

    Excepciones:
        ValueError
    """

    if monto <= 0:
        raise ValueError(
            "El monto debe ser mayor que cero."
        )


def validar_saldo(saldo, monto):
    """
    Verifica que exista saldo suficiente.

    Parámetros:
        saldo (float)
        monto (float)

    Excepciones:
        ValueError
    """

    if monto > saldo:
        raise ValueError(
            "Fondos insuficientes."
        )


def retirar_dinero(saldo, monto):
    """
    Realiza el retiro.

    Parámetros:
        saldo (float)
        monto (float)

    Retorna:
        float
    """

    validar_monto(monto)
    validar_saldo(saldo, monto)

    return saldo - monto


def consultar_saldo(saldo):
    """
    Retorna el saldo actual.

    Parámetros:
        saldo (float)

    Retorna:
        float
    """

    return saldo


def generar_resumen(moneda, monto, tipo_cambio, saldo):
    """
    Genera un resumen del retiro.

    Parámetros:
        moneda (str)
        monto (float)
        tipo_cambio (float)
        saldo (float)

    Retorna:
        dict
    """

    return {
        "moneda": moneda,
        "monto_retirado": round(monto, 2),
        "tipo_cambio": round(tipo_cambio, 2),
        "saldo_restante": round(saldo, 2)
    }