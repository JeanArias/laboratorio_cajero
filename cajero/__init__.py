"""
Paquete: cajero

Este archivo expone las funciones principales de los módulos
para facilitar su importación desde el programa principal.

"""

# ==========================
# API
# ==========================

from .api import (
    obtener_tipo_cambio,
)

# ==========================
# Operaciones
# ==========================

from .operaciones import (
    SALDO_INICIAL,
    convertir_a_colones,
    consultar_saldo,
    generar_resumen,
    retirar_dinero,
    validar_monto,
    validar_saldo,
)

# ==========================
# Menú
# ==========================

from .menu import (
    mostrar_encabezado,
    mostrar_menu,
    mostrar_saldo,
    obtener_moneda,
    leer_opcion,
    solicitar_monto,
    mostrar_tipo_cambio,
    mostrar_conversion,
    confirmar_retiro,
    preguntar_continuar,
    mostrar_retiro_exitoso,
    mostrar_despedida,
)