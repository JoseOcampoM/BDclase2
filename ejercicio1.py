from api.library import *

def main():
    SALARIO_MIN = 1000000
    SUB_ALIM = 120000
    SUB_TRANSP = 80000
    BONO = 50000
    nombre = input("Digite el Nombre ==>  ")
    salario = int(input("Digite su salario ==>  "))
    diasTrabajados = int(input("Digite cuantos dias trabajo al mes ==>  "))
    sueldoaPagar = calcularSueldo(salario, diasTrabajados)

    if salario < (SALARIO_MIN * 2):
        sueldoaPagar = sueldoaPagar + SUB_ALIM + SUB_TRANSP
    else:
        sueldoaPagar = sueldoaPagar + BONO
    

    print(f"Su nombre es {nombre} y su sueldo es de {sueldoaPagar:.0f}")



if __name__ == "__main__":
    main()