'''
Docstring para actividades.actividad02.ejercicio02.simulador_cuenta
'''
import utilidades as u
total_ingresos = 0
total_retiradas = 0
saldo = u.pedir_saldo_inicial("Introduce el saldo inicial de la cuenta: ")

while True:
    operacion = u.pedir_operacion("\n--------------------\nIntroduce la operación a realizar:\n1. Ingresar dinero\n2. Retirar dinero\n3. Mostrar saldo\n4. Estadísticas\n5. Salir\n--------------------\nOpción: ")
    if operacion == 1:
        saldo_final = u.ingresar("Introduce la cantidad a ingresar: ", saldo)
        saldo = saldo_final
        total_ingresos += 1
    elif operacion == 2:
        saldo_final = u.retirar("Introduce la cantidad a retirar: ", saldo)
        saldo = saldo_final
        total_retiradas += 1
    elif operacion == 3:
        u.mostrar_saldo(saldo)
        continue
    elif operacion == 4:
        u.estadisticas(total_ingresos, total_retiradas)
        continue
    elif operacion == 5:
        print("Saliendo del simulador de cuenta. ¡Hasta luego!")
        break
