"""

Sistema de Cajero Automático

"""

from cajero import (
    SALDO_INICIAL,
    obtener_tipo_cambio,
    convertir_a_colones,
    retirar_dinero,
    mostrar_encabezado,
    mostrar_saldo,
    mostrar_menu,
    leer_opcion,
    obtener_moneda,
    solicitar_monto,
    mostrar_tipo_cambio,
    mostrar_conversion,
    confirmar_retiro,
    preguntar_continuar,
    mostrar_retiro_exitoso,
    mostrar_despedida
)


def main():

    saldo = SALDO_INICIAL
    continuar = "S"

    while continuar.upper() == "S":

        mostrar_encabezado()
        mostrar_saldo(saldo)
        mostrar_menu()

        opcion = leer_opcion()

        # Salir
        if opcion == "0":
            break

        moneda = obtener_moneda(opcion)

        if moneda is None:
            print("\n❌ Opción inválida.")
            continue

        try:

            # Obtener tipo de cambio desde el API
            tipo_cambio = obtener_tipo_cambio(moneda)

            mostrar_tipo_cambio(moneda, tipo_cambio)

            # Solicitar monto
            monto = solicitar_monto(moneda)

            # Convertir a colones
            monto_colones = convertir_a_colones(
                monto,
                tipo_cambio
            )

            mostrar_conversion(
                moneda,
                monto,
                monto_colones
            )

            confirmar = confirmar_retiro()

            if confirmar.upper() != "S":
                print("\nOperación cancelada.")
                continue

            # Realizar retiro
            saldo = retirar_dinero(
                saldo,
                monto_colones
            )

        except ValueError as error:

            print(f"\n❌ {error}")

        except ConnectionError as error:

            print(f"\n🌐 {error}")

        except TimeoutError as error:

            print(f"\n⏱️ {error}")

        except Exception as error:

            print(f"\n⚠️ Error inesperado: {error}")

        else:

            mostrar_retiro_exitoso(saldo)

        finally:

            print("\nOperación finalizada.")

        continuar = preguntar_continuar()

    mostrar_despedida(saldo)


if __name__ == "__main__":
    main()