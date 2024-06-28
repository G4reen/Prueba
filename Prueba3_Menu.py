from Prueba3 import *
import os
import json
while True:
    os.system("cls")
    print("*"*30)
    print("*       Mundo Libro          *")
    print("*"*30)

    print("[1] - Mantenedor de categorias\n[2] - Reportes\n[3] - Salir")
    opcion = input("---> ")

    if opcion == "1":
        os.system("cls")
        print("*"*35)
        print("*     MANTENEDOR CATEGORIAS       *")
        print("*"*35)
        print("[1] - Agregar categoria\n[2] - Editar categoria\n[3] - Eliminar categoria\n[4] - Buscar categoria\n[5] - Volver")
        opcion1 = input("--->")
        if opcion1 =="1":
            agregar_categoria()
            continue
        if opcion1 =="2":
            editar_categoria()
            continue
        if opcion1 =="3":
            eliminar_categoria()
            continue
        if opcion1 =="4":
            buscar_categoria()
            continue
        if opcion1 =="5":
            pass
        else:
            print("ingresa una opcion existente")
            input("")
    
    if opcion =="2":
        os.system("cls")
        print("*"*60)
        print("*         Libro             Cantidad de veces Prestado     *")
        print("*"*60)
        with open("Reportes_biblioteca_mundo_libro.json","r") as file:
            data = json.load(file)
            for libro in data["libro"]:
                print(libro["nombre"],"",libro["veces usado"],sep="          ")
            input("")
    
    
    
    
    
    
    
    if opcion =="3":
        break