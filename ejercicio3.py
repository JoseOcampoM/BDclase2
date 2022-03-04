# *****************************************
#             manejo de listas
# *****************************************



def listas():
    lista1 = []
    lista2 = list()
    
    listaConElementos = [30, 2000000, "Jose Ocampo", "Estudiante", True, ["Magister", "Doctorado", "Especializacion", 20]]
    
    #print(listaConElementos[1])
    
    #Utiliizando el ciclo for
    print("Mostrando elementos con ciclo for")
    for i in range(len(listaConElementos)):
        print(listaConElementos[i])
        
    
    #Utilizando El ciclo while
    print("Mostrando elementos con ciclo while" )
    j=0
    while j < len(listaConElementos):
        print(listaConElementos[j])
        j+=1
        
    print(listaConElementos[5][3])
    print(listaConElementos[-1][3])
    print(listaConElementos[0:3]) #Miuestra la posicion de la 0 hasta la 3 sin entrar la 3
    print(listaConElementos[1:6:2])
    print(listaConElementos[0:6:2])

def main():
    listas()
    
    
if __name__ == "__main__":
    main()