import json
import os
def agregar_categoria():
    categoria_add = input("Ingrese el nombre que desea agregar: ")
    with open("biblioteca.json", "r") as file:
        data = json.load(file)
        data["Categoria"].append({
            "CategoriaID": len(data["Categoria"])+1,
            "Nombre" : categoria_add

        })
        print("Se agrego la categoria Correctamente, Presiona Enter para continuar"),input()
        with open("biblioteca.json","w") as file:
            json.dump(data,file,indent=4)


def editar_categoria():
    with open("biblioteca.json", "r") as file:
        data = json.load(file)
        categoria_edit = input("Ingrese el id de la categoria que desea editar: ")
        for categoria in data["Categoria"]:
            if categoria["CategoriaID"] == int(categoria_edit):
                categoria["Nombre"] = input("Ingrese el nuevo nombre de la categoria: ")
                print("Se edito la categoria correctamente, presione Enter para continuar"),input()
        with open("biblioteca.json", "w") as file:
            json.dump(data,file,indent=4)


def eliminar_categoria():
    with open("biblioteca.json", "r") as file:
        data = json.load(file)
        categoria_delete = input("Ingrese el id de la categoria que desea eliminar: ")
        for categoria in data["Categoria"]:
            if categoria["CategoriaID"] == int(categoria_delete):
                data["Categoria"].remove(categoria)
                print("Se elimino la categoria",categoria["Nombre"],"Presiona Enter para continuar"),input()
        with open("biblioteca.json", "w") as file:
            json.dump(data,file,indent=4)

def buscar_categoria():
    with open("biblioteca.json","r") as file:
        data=json.load(file)
        categoria_buscar = int(input("Ingrese la id de la categoria que desea Buscar: "))
        for categoria in data["Categoria"]:
            if categoria["CategoriaID"] == categoria_buscar:
                print("ID: ",categoria["CategoriaID"], "\nNombre: ",categoria["Nombre"])
                input("Presiona Enter para continuar")
                break