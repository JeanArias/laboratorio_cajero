SALDO_INICIAL = 1000000

from cajero.operaciones import retirar_dinero, FondosInsuficientesError, MontoMinimoError

def main():
    saldo_actual = SALDO_INICIAL
    
    # 1. Solicitar el monto de retiro
    monto_input = input("Ingrese el monto a retirar (Mínimo $10): ")
    
    try:
        # Intentar convertir la entrada a número (falla con letras o símbolos)
        monto = float(monto_input)
        
        # Validar el retiro y descontar del saldo
        nuevo_saldo = retirar_dinero(saldo_actual, monto)

    except ValueError:
        # Se activa si el usuario ingresó letras, texto o símbolos en lugar de números
        print("\n[ERROR DE ENTRADA] Has ingresado un dato no válido. Debes introducir únicamente un número entero o decimal.")

    except MontoMinimoError as error_monto_minimo:
        # Se activa si el monto ingresado es inferior a 10 (incluye números negativos o cero)
        print(f"\n[ERROR DE REGLA DE NEGOCIO] {error_monto_minimo}")

    except FondosInsuficientesError as error_fondos:
        # Se activa si el saldo en la cuenta es inferior al monto solicitado
        print(f"\n[ERROR DE SALDO] {error_fondos}")

    else:
        # Se ejecuta SOLO SI NO HUBO ERRORES durante la transacción
        saldo_actual = nuevo_saldo
        print(f"\n[OPERACIÓN EXITOSA] Has retirado: ${monto:,.2f}")

    finally:
        # Se ejecuta SIEMPRE al finalizar, ocurra un error o no
        print(f"\n[RESUMEN] Saldo disponible en cuenta: ${saldo_actual:,.2f}")
        print("Gracias por utilizar el Cajero Automático.")

if __name__ == "__main__":
    main()