from api.library import *

def main():
# #aplicacion de los diccionarios
#     persona = {
#         "nombre": "Jose",
#         "apellidos": "Ocampo",
#         "Edad": 24
    
#     }
    persona ={
        "datospersonales":{
            "nombre": "Jose",
            "apellido": "Ocampo",
            "edad": 24
        },
            
        "salarial": {
            "salario": 2000000,
            "subtransporte": 50000,
            "subalimentacion": 60000
        }
    }    
    # print(persona["nombre"]+ " "+ persona)["apellidos"]
    
    #print(f"{persona['nombre']} {persona['apellidos']}")
    print(f"nombre: {persona['datospersonales']['nombre']} {persona['datospersonales']['apellido']}")
    

if __name__ == "__main__":
    main()