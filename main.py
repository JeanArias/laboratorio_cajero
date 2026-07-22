"""
main.py

Sistema de Cajero Automático.

Autor: ___________________
Curso: Fundamentos de Python 2
"""

from cajero.operaciones import SALDO_INICIAL, retirar_dinero



def main():

    saldo = SALDO_INICIAL
    continuar = "S"

    print("=" * 50)
    print("      SISTEMA DE CAJERO AUTOMÁTICO")
    print("=" * 50)

    while continuar.upper() == "S":

        print(f"\nSaldo disponible: ₡{saldo:,.0f}")

        try:

            monto = float(
                input("¿Cuánto desea retirar? ₡")
            )

            saldo = retirar_dinero(saldo, monto)

        except ValueError as error:

            if "could not convert string" in str(error):

                print("\n❌ Debe ingresar un número.")

            elif str(error) == "El monto no puede ser negativo.":

                print("\n❌ Monto inválido.")

            elif str(error) == "Fondos insuficientes.":

                print("\n❌ Fondos insuficientes.")

            else:

                print(f"\n❌ Error: {error}")

        else:

            print("\n✅ Retiro realizado correctamente.")
            print(f"Saldo restante: ₡{saldo:,.0f}")

            if saldo == 0:
                print("\nLa cuenta quedó sin fondos.")
                break

        finally:

            print("\nOperación finalizada.")

        continuar = input(
            "\n¿Desea realizar otro retiro? (S/N): "
        )

    print("\n" + "=" * 50)
    print("Gracias por utilizar el cajero.")
    print(f"Saldo final: ₡{saldo:,.0f}")
    print("=" * 50)


if __name__ == "__main__":
    main()