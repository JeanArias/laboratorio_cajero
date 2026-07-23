"""

Contiene las funciones relacionadas con la interfaz
del usuario del Cajero Automático.

"""


def mostrar_encabezado():
    """Muestra el encabezado del sistema."""

    print("\n" + "=" * 50)
    print("         CAJERO AUTOMÁTICO")
    print("=" * 50)


def mostrar_saldo(saldo):
    """
    Muestra el saldo disponible.

    Parámetros:
        saldo (float)
    """

    print(f"\nSaldo disponible: ₡{saldo:,.2f}")


def mostrar_menu():
    """
    Muestra el menú principal.
    """

    print("\nSeleccione la moneda para el retiro:")
    print("1. Colones (CRC)")
    print("2. Dólares (USD)")
    print("3. Euros (EUR)")
    print("0. Salir")


def leer_opcion():
    """
    Solicita la opción del menú.

    Retorna:
        str
    """

    return input("\nSeleccione una opción: ")


def obtener_moneda(opcion):
    """
    Convierte la opción seleccionada
    en el código de la moneda.

    Parámetros:
        opcion (str)

    Retorna:
        str | None
    """

    monedas = {
        "1": "CRC",
        "2": "USD",
        "3": "EUR"
    }

    return monedas.get(opcion)


def solicitar_monto(moneda):
    """
    Solicita el monto que desea retirar.

    Parámetros:
        moneda (str)

    Retorna:
        float
    """

    return float(
        input(f"\n¿Cuántos {moneda} desea retirar?: ")
    )


def mostrar_tipo_cambio(moneda, tipo_cambio):
    """
    Muestra el tipo de cambio obtenido
    desde el API.

    Parámetros:
        moneda (str)
        tipo_cambio (float)
    """

    if moneda != "CRC":
        print(f"\nTipo de cambio actual")
        print(f"1 {moneda} = ₡{tipo_cambio:,.2f}")


def mostrar_conversion(moneda, monto, colones):
    """
    Muestra la conversión realizada.

    Parámetros:
        moneda (str)
        monto (float)
        colones (float)
    """

    if moneda != "CRC":
        print(f"\n{monto:,.2f} {moneda} = ₡{colones:,.2f}")


def confirmar_retiro():
    """
    Solicita confirmar el retiro.

    Retorna:
        str
    """

    return input("\n¿Desea confirmar el retiro? (S/N): ")


def preguntar_continuar():
    """
    Pregunta si desea realizar otro retiro.

    Retorna:
        str
    """

    return input("\n¿Desea realizar otro retiro? (S/N): ")


def mostrar_retiro_exitoso(saldo):
    """
    Muestra el resultado de un retiro exitoso.

    Parámetros:
        saldo (float)
    """

    print("\n✅ Retiro realizado correctamente.")
    print(f"Saldo restante: ₡{saldo:,.2f}")


def mostrar_despedida(saldo):
    """
    Muestra el mensaje de salida.

    Parámetros:
        saldo (float)
    """

    print("\n" + "=" * 50)
    print("Gracias por utilizar el Cajero Automático.")
    print(f"Saldo final: ₡{saldo:,.2f}")
    print("=" * 50)