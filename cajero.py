import mysql.connector
import hashlib

def inicio():
    print("Bienvenido")
    print("¿En qué le puedo ayudar?")
    print("1. Depositar dinero")  
    print("2. Mostrar saldo")
    print("3. Retirar efectivo")
    print("4. Realizar avances en efectivo")
    print("5. Transferencias")
    print("6. Pago de servicios")
    print("7. Cambiar clave principal")
    print("8. Salir")

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="cajero_automatico"
    )

def depositar(cuenta_id, valor):
    mydb = conectar()
    cursor = mydb.cursor()
    
    sql = "UPDATE cuentas SET saldo = saldo + %s WHERE id = %s"
    cursor.execute(sql, (valor, cuenta_id))
    mydb.commit()

    cursor.execute("SELECT saldo FROM cuentas WHERE id = %s", (cuenta_id,))
    nuevo_saldo = cursor.fetchone()[0]

    cursor.close()
    mydb.close()

    print("El saldo nuevo es:", nuevo_saldo)
    return nuevo_saldo

def retirar(cuenta_id, valor):
    mydb = conectar()
    cursor = mydb.cursor()

    cursor.execute("SELECT saldo FROM cuentas WHERE id = %s", (cuenta_id,))
    saldo_actual = cursor.fetchone()[0]

    if valor <= saldo_actual:
        sql = "UPDATE cuentas SET saldo = saldo - %s WHERE id = %s"
        cursor.execute(sql, (valor, cuenta_id))
        mydb.commit()

        cursor.execute("SELECT saldo FROM cuentas WHERE id = %s", (cuenta_id,))
        nuevo_saldo = cursor.fetchone()[0]

        print("El saldo nuevo es:", nuevo_saldo)
        return nuevo_saldo
    else:
        print("Su saldo es insuficiente")
        return saldo_actual

    cursor.close()
    mydb.close()

def avances_efectivo(cuenta_id, valor):
    mydb = conectar()
    cursor = mydb.cursor()

    cursor.execute("SELECT saldo FROM cuentas WHERE id = %s", (cuenta_id,))
    saldo = cursor.fetchone()[0]

    if valor <= saldo:
        sql = "UPDATE cuentas SET saldo = saldo - %s WHERE id = %s"
        cursor.execute(sql, (valor, cuenta_id))
        mydb.commit()

        cursor.execute("SELECT saldo FROM cuentas WHERE id = %s", (cuenta_id,))
        nuevo_saldo_disponible = cursor.fetchone()[0]

        print("El saldo disponible nuevo es:", nuevo_saldo_disponible)
        return nuevo_saldo_disponible
    else:
        print("Su saldo disponible es insuficiente")
        return saldo

    cursor.close()
    mydb.close()

def transferencias(cuenta_id_origen, valor, cuenta_id_destino):
    mydb = conectar()
    cursor = mydb.cursor()

    cursor.execute("SELECT saldo FROM cuentas WHERE id = %s", (cuenta_id_origen,))
    saldo_origen = cursor.fetchone()[0]

    if valor <= saldo_origen:
        sql = "UPDATE cuentas 5 saldo = saldo - %s WHERE id = %s"
        cursor.execute(sql, (valor, cuenta_id_origen))

        cursor.execute("SELECT id FROM cuentas WHERE id = %s", (cuenta_id_destino,))
        cuenta_destino_existe = cursor.fetchone() is not None

        if cuenta_destino_existe:
            sql = "UPDATE cuentas SET saldo = saldo + %s WHERE id = %s"
            cursor.execute(sql, (valor, cuenta_id_destino))
            mydb.commit()

            print("Transferencia de $", valor, "a la cuenta", cuenta_id_destino, "realizada correctamente")

            cursor.execute("SELECT saldo FROM cuentas WHERE id = %s", (cuenta_id_origen,))
            nuevo_saldo_origen = cursor.fetchone()[0]
            cursor.execute("SELECT saldo FROM cuentas WHERE id = %s", (cuenta_id_destino,))
            nuevo_saldo_destino = cursor.fetchone()[0]

            print("El saldo nuevo de la cuenta", cuenta_id_origen, "es:", nuevo_saldo_origen)
            print("El saldo nuevo de la cuenta", cuenta_id_destino, "es:", nuevo_saldo_destino)

            return nuevo_saldo_origen, nuevo_saldo_destino
        else:
            print("La cuenta destino no existe")
            return saldo_origen, saldo_origen
    else:
        print("Su saldo en la cuenta origen es insuficiente")
        return saldo_origen, saldo_origen

    cursor.close()
    mydb.close()

def servicios(cuenta_id, servicio, valor):
    mydb = conectar()
    cursor = mydb.cursor()

    cursor.execute("SELECT saldo FROM cuentas WHERE id = %s", (cuenta_id,))
    saldo_actual = cursor.fetchone()[0]

    if valor <= saldo_actual:
        sql = "UPDATE cuentas SET saldo = saldo - %s WHERE id = %s"
        cursor.execute(sql, (valor, cuenta_id))
        mydb.commit()

        print("Pago de", valor, "para", servicio, "realizado con éxito")

        cursor.execute("SELECT saldo FROM cuentas WHERE id = %s", (cuenta_id,))
        nuevo_saldo = cursor.fetchone()[0]

        print("El saldo nuevo es:", nuevo_saldo)
        return nuevo_saldo
    else:
        print("Su saldo es insuficiente")
        return saldo_actual

    cursor.close()
    mydb.close()

def cambiar_clave(cuenta_id, clave_actual, nueva_clave):
    mydb = conectar()
    cursor = mydb.cursor()

    cursor.execute("SELECT clave FROM cuentas WHERE id = %s", (cuenta_id,))
    clave_actual_registrada = cursor.fetchone()[0]

    if hashlib.sha256(clave_actual.encode()).hexdigest() == clave_actual_registrada:
        nueva_clave_encriptada = hashlib.sha256(nueva_clave.encode()).hexdigest()

        sql = "UPDATE cuentas SET clave = %s WHERE id = %s"
        cursor.execute(sql, (nueva_clave_encriptada, cuenta_id))
        mydb.commit()

        print("Clave cambiada con éxito")
    else:
        print("La clave actual es incorrecta")

    cursor.close()
    mydb.close()

def saldo(cuenta_id):
    mydb = conectar()
    cursor = mydb.cursor()

    cursor.execute("SELECT saldo FROM cuentas WHERE id = %s", (cuenta_id,))
    saldo_actual = cursor.fetchone()[0]

    print("El saldo de su cuenta es:", saldo_actual)

    cursor.close()
    mydb.close()

    return saldo_actual

def mostrar_servicios():
    print("Servicios disponibles:")
    print("1. Electricidad")
    print("2. Agua")
    print("3. Teléfono")
    print("4. Internet")

def salir():
    print("Saliendo del cajero automático...")
    exit()

saldo = 0

while True:
    inicio()
    opcion = int(input("Ingrese la opción que desea realizar a continuación: "))
    if opcion == 1:
        valor = float(input("Ingrese el monto a depositar: "))
        saldo = depositar(1, valor)
    elif opcion == 2:
        saldo(1)
    elif opcion == 3:
        valor = float(input("Ingrese el monto a retirar: "))
        saldo = retirar(1, valor)
    elif opcion == 4:
        valor = float(input("Ingrese el monto del avance en efectivo: "))
        saldo = avances_efectivo(1, valor)
    elif opcion == 5: 
        valor = float(input("Ingrese el monto de la transferencia: "))
        cuenta_destino = int(input("Ingrese el id de la cuenta destino: "))
        saldo = transferencias(1, valor, cuenta_destino)
    elif opcion == 6:
        mostrar_servicios()
        servicio_elegido = int(input("Seleccione el servicio que desea pagar: "))
        if servicio_elegido == 1:
            servicio = "Electricidad"
        elif servicio_elegido == 2:
            servicio = "Agua"
        elif servicio_elegido == 3:
            servicio = "Teléfono"
        elif servicio_elegido == 4:
            servicio = "Internet"
        else:
            print("Servicio no válido")
            continue
        valor = float(input("Ingrese el monto a pagar: "))
        saldo = servicios(1, servicio, valor)
    elif opcion == 7:
        clave_actual = input("Ingrese su clave actual: ")
        nueva_clave = input("Ingrese su nueva clave: ")
        cambiar_clave(1, clave_actual, nueva_clave)
    elif opcion == 8:
        salir()
    else:
        print("Esa no es una opción válida")
