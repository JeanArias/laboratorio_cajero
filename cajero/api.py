"""
API utilizada:
https://open.er-api.com/v6/latest/USD

"""

import requests

URL_API = "https://open.er-api.com/v6/latest/"


def obtener_tipo_cambio(moneda):
    """
    Obtiene el tipo de cambio hacia Colones (CRC).
    """

    moneda = moneda.upper()

    if moneda == "CRC":
        return 1.0

    try:

        respuesta = requests.get(
            URL_API + moneda,
            timeout=10
        )

        respuesta.raise_for_status()

        datos = respuesta.json()

        if datos["result"] != "success":
            raise ValueError("No fue posible obtener el tipo de cambio.")

        return datos["rates"]["CRC"]

    except requests.ConnectionError:
        raise ConnectionError(
            "No fue posible conectarse al servidor."
        )

    except requests.Timeout:
        raise TimeoutError(
            "La solicitud tardó demasiado."
        )

    except KeyError:
        raise ValueError(
            "La respuesta del API no contiene la moneda solicitada."
        )

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