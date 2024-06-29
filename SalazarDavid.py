'''
1.	Asignar saldos aleatorios: Generar saldos aleatorios para 10 clientes.
2.	Clasificar saldos: Mostrar los saldos clasificados en tres rangos específicos.
3.	Ver estadísticas: Calcular y mostrar estadísticas avanzadas sobre los saldos.
    a.	Saldo más alto
    b.	Saldo más bajo
    c.	Saldo promedio
    d.	Media geométrica.
4.	Reporte de saldos: Generar un reporte detallado de saldos con deducciones por diferentes conceptos y saldo neto, y exportar a un archivo CSV.
5.  Salir del programa: Opción para salir del programa con un mensaje de despedida.
'''
import random, csv, os, time
from statistics import geometric_mean


def generadorSaldo():
    saldo=random.randrange(1000,1500000,1050)
    return saldo

def menu():
    print("//","-"*51,"//")
    print("//Bienvenido a Analisis y gestion de datos financieros//")
    print("//","-"*51,"//")
    print("\n1- Ingresar datos de 10 clientes (Nombre + asignacion de saldos)")
    print("\n2- Clasificar Saldos")
    print("\n3- Ver estadisticas")
    print("\n4- Reporte de saldos")
    print("\n5- Salir del programa")

def lp():
    os.system("cls")
    return

def esp(tim):
    time.sleep(tim)

def dtoCliente(NumCli):
    name=input(f"\nIngrese nombre del cliente {NumCli}: ")
    return name

def ClasifSaldos(tipo):
    clienteRango={}
    if tipo==1:    
        for c, s in clientesSaldos.items():
            if s>=1000000:
                clienteRango[c]=s
    if tipo==2:    
        for c, s in clientesSaldos.items():
            if s>=500000 and s<1000000:
                clienteRango[c]=s
    if tipo==3:
        for c, s in clientesSaldos.items():
            if s<500000:
                clienteRango[c]=s

    return clienteRango
def SoloSaldo(a):
    saldo=list(clientesSaldos.values())
    if a == 1:
        saldoFin=max(saldo)
    if a == 2:
        saldoFin=min(saldo)
    if a == 3:
        saldoFin=round(sum(saldo)/len(saldo))
    if a == 4:
        try:
            saldoFin= geometric_mean(saldo)
        except:
            saldoFin=0

    return saldoFin

clientesSaldos={-1:0}
on=1
lp()
while on==1:
    try:
        while True:
            print("\n")
            menu()
            el=int(input("\nSeleccione una opcion: "))
            if el > 5 or el < 1:
                print("Ingrese un numero de los expresados en las opciones...")
                esp(2)
                lp()
            else:
                lp()
                break
        if el == 1:
            clientesSaldos={}
            for i in range (10):
                cliente=dtoCliente(i+1)
                saldo=generadorSaldo()
                clientesSaldos[cliente]=saldo
            print("\nLos clientes han sido añadidos exitosamente, junto a sus saldos!!")
            esp(3)
            lp()
        if el == 2:
            esp(1)
            print("\nClasificacion de saldos mayores o iguales a $1.000.000")
            clientesAltos=ClasifSaldos(1)
            for c,s in clientesAltos.items():
                print(f"- Cliente: {c} Saldo: {s}")

            print("\nClasificacion de saldos mayores o iguales a $500.000")
            clientesMedios=ClasifSaldos(2)
            for c,s in clientesMedios.items():
                print(f"- Cliente: {c} Saldo: {s}")

            print("\nClasificacion de saldos menores a $500.000")
            clientesBajos=ClasifSaldos(3)
            for c,s in clientesBajos.items():
                print(f"- Cliente: {c} Saldo: {s}")
            esp(2)
        if el == 3:
            esp(1)
            print("\nEstadisticas: ")
            esp(1)
            print(f"a. Saldo mas alto: {SoloSaldo(1)}")
            print(f"b. Saldo mas bajo: {SoloSaldo(2)}")
            print(f"c. Saldo promedio: {SoloSaldo(3)}")
            print(f"d. Media Geometrica: {SoloSaldo(4)}")
            esp(2)
        if el == 4:
            esp(1)
            report=clientesSaldos.items()
            with open("Reporte Financiero.csv", mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(report)
            esp(1)
            print("\nReporte guardado exitosamente...")
            esp(2)
            print("\nReporte Financiero: ")
            with open('Reporte Financiero.csv', mode='r', newline='') as file:
                reader = csv.reader(file)
                rows = list(reader)
            for row in rows:
                print(row)
        if el == 5:
            esp(1)
            print("Cerrando programa, espero tenga un buen dia...")
            esp(2)
            on=0
            break
                

    except:
            
    
        print("Ingrese un numero...")
        esp(2)
        lp()
